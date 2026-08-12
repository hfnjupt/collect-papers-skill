#!/usr/bin/env python3
"""Audit local PDFs for code links and safely quarantine or delete reviewed files."""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    from pypdf import PdfReader
except ImportError as exc:
    raise SystemExit("pypdf is required. Run this script with the bundled PDF Python runtime.") from exc


URL_RE = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<>{}\[\]\"']+")
BARE_REPO_RE = re.compile(
    r"(?i)\b(?:github\.com|gitlab\.com|bitbucket\.org|codeberg\.org|gitee\.com)"
    r"/[A-Za-z0-9_.~-]+/[A-Za-z0-9_.~-]+(?:/[^\s<>{}\[\]\"']*)?"
)
CODE_CUE_RE = re.compile(
    r"(?i)\b(source\s+code|codebase|implementation|repository|repo|github|gitlab|"
    r"code\s+is|code\s+at|代码|源码|实现代码|代码仓库|项目仓库)\b"
)
REPO_HOSTS = {
    "github.com",
    "www.github.com",
    "gitlab.com",
    "www.gitlab.com",
    "bitbucket.org",
    "www.bitbucket.org",
    "codeberg.org",
    "www.codeberg.org",
    "gitee.com",
    "www.gitee.com",
    "sourceforge.net",
    "www.sourceforge.net",
}
REPORT_FIELDS = [
    "relative_path",
    "status",
    "text_chars",
    "matched_links",
    "evidence",
    "error",
    "size_bytes",
    "mtime_ns",
]


def clean_url(value: str) -> str:
    value = value.strip().rstrip(".,;:!?)]}>'\"")
    if value.lower().startswith("www."):
        value = "https://" + value
    if not re.match(r"(?i)^https?://", value):
        value = "https://" + value
    return value


def is_repository_url(value: str) -> bool:
    parsed = urlparse(clean_url(value))
    host = parsed.netloc.lower()
    parts = [part for part in parsed.path.split("/") if part]
    if host in {"sourceforge.net", "www.sourceforge.net"}:
        return len(parts) >= 2 and parts[0].lower() == "projects"
    return host in REPO_HOSTS and len(parts) >= 2


def extract_pdf(path: Path) -> tuple[str, list[str], str]:
    try:
        reader = PdfReader(str(path))
        if reader.is_encrypted:
            try:
                if reader.decrypt("") == 0:
                    return "", [], "encrypted PDF"
            except Exception:
                return "", [], "encrypted PDF"

        texts: list[str] = []
        annotations: list[str] = []
        for page in reader.pages:
            texts.append(page.extract_text() or "")
            for annot_ref in page.get("/Annots", []) or []:
                try:
                    annot = annot_ref.get_object()
                    action = annot.get("/A")
                    uri = action.get("/URI") if action else None
                    if uri:
                        annotations.append(str(uri))
                except Exception:
                    continue
        return "\n".join(texts), annotations, ""
    except Exception as exc:
        return "", [], f"{type(exc).__name__}: {exc}"


def find_code_links(text: str, annotations: list[str], contextual: bool) -> tuple[list[str], list[str]]:
    links: dict[str, str] = {}

    for match in BARE_REPO_RE.finditer(text):
        link = clean_url(match.group(0))
        links[link] = "repository URL in extracted text"

    for match in URL_RE.finditer(text):
        raw = match.group(0)
        link = clean_url(raw)
        if is_repository_url(link):
            links[link] = "repository URL in extracted text"
            continue
        if contextual:
            window = text[max(0, match.start() - 180) : min(len(text), match.end() + 180)]
            if CODE_CUE_RE.search(window):
                links[link] = "contextual code URL in extracted text"

    for raw in annotations:
        link = clean_url(raw)
        if is_repository_url(link):
            links[link] = "repository URL in PDF link annotation"

    return sorted(links), [links[link] for link in sorted(links)]


def enumerate_pdfs(root: Path, recursive: bool) -> list[Path]:
    candidates = root.rglob("*") if recursive else root.glob("*")
    return sorted(
        (
            path
            for path in candidates
            if path.is_file() and not path.is_symlink() and path.suffix.lower() == ".pdf"
        ),
        key=str,
    )


def scan(root: Path, recursive: bool, contextual: bool, min_chars: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in enumerate_pdfs(root, recursive):
        stat = path.stat()
        text, annotations, error = extract_pdf(path)
        links, evidence = find_code_links(text, annotations, contextual)
        if error or len(text.strip()) < min_chars:
            status = "needs_review"
            if not error:
                error = f"extracted text below threshold ({len(text.strip())} < {min_chars})"
        elif links:
            status = "has_code"
        else:
            status = "no_code"
        rows.append(
            {
                "relative_path": str(path.relative_to(root)),
                "status": status,
                "text_chars": str(len(text.strip())),
                "matched_links": " | ".join(links),
                "evidence": " | ".join(dict.fromkeys(evidence)),
                "error": error,
                "size_bytes": str(stat.st_size),
                "mtime_ns": str(stat.st_mtime_ns),
            }
        )
    return rows


def write_report(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=REPORT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def load_reviewed_no_code(root: Path, report: Path) -> list[tuple[Path, dict[str, str]]]:
    targets: list[tuple[Path, dict[str, str]]] = []
    with report.open("r", encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            if row.get("status") != "no_code":
                continue
            candidate = (root / row["relative_path"]).resolve()
            try:
                candidate.relative_to(root)
            except ValueError as exc:
                raise SystemExit(f"Report path escapes input directory: {candidate}") from exc
            if not candidate.is_file() or candidate.suffix.lower() != ".pdf":
                raise SystemExit(f"Reported PDF is missing or invalid: {candidate}")
            stat = candidate.stat()
            if stat.st_size != int(row["size_bytes"]) or stat.st_mtime_ns != int(row["mtime_ns"]):
                raise SystemExit(f"PDF changed after the report was created; re-scan it: {candidate}")
            targets.append((candidate, row))
    return targets


def apply_quarantine(root: Path, targets: list[tuple[Path, dict[str, str]]], destination: Path) -> None:
    destination = destination.resolve()
    try:
        destination.relative_to(root)
    except ValueError:
        pass
    else:
        raise SystemExit("Quarantine directory must be outside the input directory.")
    moves = [(source, destination / row["relative_path"]) for source, row in targets]
    for _source, target in moves:
        if target.exists():
            raise SystemExit(f"Refusing to overwrite quarantine target: {target}")
    for source, target in moves:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source), str(target))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", type=Path, help="Directory containing downloaded PDF papers")
    parser.add_argument("--output", type=Path, help="CSV report path; defaults inside input_dir")
    parser.add_argument("--no-recursive", action="store_true", help="Scan only the top-level directory")
    parser.add_argument("--contextual", action="store_true", help="Accept non-repository URLs near code cues")
    parser.add_argument("--min-chars", type=int, default=300, help="Minimum extracted characters for no_code")
    parser.add_argument("--action", choices=("report", "quarantine", "delete"), default="report")
    parser.add_argument("--from-report", type=Path, help="Reviewed CSV required for quarantine or deletion")
    parser.add_argument("--quarantine-dir", type=Path, help="Destination for quarantine mode")
    parser.add_argument("--confirm", help="Required confirmation token for mutating actions")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.input_dir.resolve()
    if not root.is_dir():
        raise SystemExit(f"Input directory does not exist: {root}")

    if args.action == "report":
        output = (args.output or (root / "code-link-audit.csv")).resolve()
        rows = scan(root, not args.no_recursive, args.contextual, args.min_chars)
        write_report(output, rows)
        counts = {state: sum(row["status"] == state for row in rows) for state in ("has_code", "no_code", "needs_review")}
        print(f"Scanned {len(rows)} PDFs: {counts}. Report: {output}")
        return 0

    if not args.from_report or not args.from_report.is_file():
        raise SystemExit("Mutating actions require --from-report pointing to a reviewed CSV.")
    targets = load_reviewed_no_code(root, args.from_report.resolve())
    print(f"Reviewed no_code targets: {len(targets)}")

    if args.action == "quarantine":
        if args.confirm != "REVIEWED_NO_CODE_REPORT":
            raise SystemExit("Quarantine requires --confirm REVIEWED_NO_CODE_REPORT")
        destination = args.quarantine_dir or root.with_name(root.name + "-no-code-quarantine")
        apply_quarantine(root, targets, destination)
        print(f"Quarantined {len(targets)} PDFs to {destination.resolve()}")
        return 0

    if args.confirm != "DELETE_NO_CODE_PDFS":
        raise SystemExit("Permanent deletion requires --confirm DELETE_NO_CODE_PDFS")
    for target, _row in targets:
        print(f"Deleting: {target}")
    for target, _row in targets:
        target.unlink()
    print(f"Permanently deleted {len(targets)} reviewed PDFs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
