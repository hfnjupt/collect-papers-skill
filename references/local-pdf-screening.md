# Local PDF Code-Link Screening

## Evidence levels

Use one of these matching policies and report which one was applied:

- **Strict**: Accept only repository URLs on recognized code hosts, such as GitHub, GitLab, Bitbucket, Codeberg, Gitee, or SourceForge.
- **Contextual**: Also accept another URL when nearby PDF text explicitly says code, source code, implementation, repository, Git, or an equivalent phrase.
- **Verified**: Start with strict or contextual matches, then open each candidate and confirm that it resolves to an accessible code repository. Report inaccessible and authentication-gated links separately.

Do not silently treat Papers with Code pages, DOI links, dataset pages, model cards, author homepages, or generic project pages as source-code repositories. A project page counts only when the paper identifies it as the code location or the page exposes a repository link that is verified.

## Required triage states

Classify every PDF into exactly one state:

| State | Meaning | Eligible for automatic cleanup |
|---|---|---|
| `has_code` | At least one qualifying code link was detected | No |
| `no_code` | Text extraction succeeded and no qualifying link was detected | Only after report review |
| `needs_review` | The file is scanned, extraction-poor, encrypted, unreadable, or otherwise uncertain | Never |

Inspect `needs_review` PDFs visually or with OCR. Check appendices, footnotes, supplementary sections, and PDF hyperlink annotations. Broken line wrapping can split URLs across text runs.

## Safe two-phase cleanup

Always separate detection from mutation:

1. Generate a CSV report without moving or deleting files.
2. Review all `needs_review` rows and suspicious `no_code` rows.
3. Preserve the report as the decision manifest.
4. Apply quarantine or deletion only from that report.
5. Require the current file size and modification timestamp to equal the reviewed values. Re-scan changed files.

Default to quarantine in a sibling directory named `<input>-no-code-quarantine`. Preserve relative subdirectories. If a destination file already exists, stop rather than overwrite it.

Permit permanent deletion only after an explicit user request in the current task. State the exact number and paths targeted before deletion. Use the script's `DELETE_NO_CODE_PDFS` confirmation token. Report that permanent deletion is not recoverable through the skill.

## Interpreting code availability

Distinguish these claims:

- **Address present**: The PDF prints or embeds a qualifying URL.
- **Repository reachable**: The URL responded when checked.
- **Code available**: The destination appears to contain source code rather than only a landing page, weights, data, or a promise of future release.
- **Code usable**: Licensing, dependencies, instructions, and artifacts are sufficient to run it. Do not infer this from the URL alone.

When the user only asks whether an address is present, do not reject a paper solely because the link is temporarily unreachable. When the user asks for usable code, inspect repository contents and record the verification date.
