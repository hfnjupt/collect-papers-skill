---
name: collect-papers
description: Search, verify, filter, deduplicate, and organize academic papers by topic, keyword, author, author plus organization, or authors identified from a known paper; prioritize major communications, networking, computer-vision, AI, machine-learning, multimedia, and systems venues; build a high-coverage publication set for a disambiguated author; audit downloaded PDFs for code links; and export streamlined paper metadata and translated abstracts to Excel. Use when the user asks to 搜集论文、查找文献、按关键词或作者检索、限定作者单位、从一篇论文追踪作者全部论文、追踪代表性或最新工作、优先顶会顶刊、制作论文清单、导出含摘要及翻译的 Excel、筛选带代码论文、遍历本地论文 PDF、隔离或删除没有代码地址的论文, build a related-work reading list, or export verified citation metadata. Supports year and venue filters, author identity resolution, online bibliographic search, full-text PDF screening, spreadsheet export, and guarded cleanup across disciplines.
---

# Collect Papers

## Goal

Build a reproducible, source-linked paper set rather than an unverified list. Search broadly enough to reduce obvious blind spots, then verify every included record against a primary or authoritative bibliographic source.

## Establish the scope

Extract or infer these constraints before searching:

- Research direction, question, or exact keyword expression
- Publication years or recency requirement
- Disciplines, venues, paper types, and languages
- Whether venue preference is soft priority or a strict venue-only filter
- Desired count and ranking preference
- Required output fields and export format
- Whether the task is online bibliographic search or downloaded/full-text paper inspection
- Inclusion and exclusion rules
- Local PDF directory, code-link matching strictness, and cleanup policy when auditing downloads
- Author name, organization, known-paper seed, target author role, and identity confidence when searching by author

Ask one concise question only when a missing constraint would materially change the result. Otherwise state reasonable assumptions and proceed. Treat quoted text as an exact phrase; treat unquoted concepts as expandable topics.

## Build the query set

Create a small query matrix before browsing:

1. Preserve the user's exact terms.
2. Add common aliases, abbreviations, spelling variants, and translated terms.
3. Add one or two broader parent concepts for recall.
4. Add narrower methods, tasks, datasets, or applications for precision.
5. Add exclusion terms only after inspecting early false positives.

For a broad direction, search several concept combinations rather than one long query. For an exact keyword request, separate papers that contain the literal phrase in the title or abstract from papers that are merely conceptually relevant.

Read [references/search-strategy.md](references/search-strategy.md) when choosing databases, adapting queries by discipline, or resolving conflicting metadata. For communications, networking, wireless, multimedia, image/video, computer vision, AI, machine learning, data mining, web, or computer-systems requests, also read [references/priority-venues.md](references/priority-venues.md) and apply only its relevant topical venue groups unless the user supplies a different venue policy.

## Apply venue priority

For communications and computer-domain searches, treat the bundled mainstream journal and conference profile as a soft priority by default. Select venue groups by topic; do not search every computer venue for every request:

1. Search the priority venues first with canonical titles and verified aliases.
2. Search broader scholarly sources afterward to catch relevant papers outside the profile.
3. Rank equally relevant papers from priority venues ahead of other venues, while preserving relevance and identity confidence as the stronger criteria.
4. Report which priority venues were searched and whether broader expansion produced additional papers.

Examples of topical routing:

- Computer vision, image understanding, detection, segmentation, or 3D vision: prioritize CVPR, ICCV, ECCV, and WACV, plus relevant multimedia/image venues.
- General machine learning or representation learning: prioritize NeurIPS, ICML, and ICLR; include AAAI/IJCAI when broadly relevant.
- Multimedia: prioritize ACM Multimedia, ACM MMSys, ICME, and the relevant multimedia/image journals.
- Data mining and web: prioritize KDD and The Web Conference.
- Computer systems and networking: prioritize SIGCOMM, NSDI, OSDI, SOSP, EuroSys, USENIX ATC, INFOCOM, MobiCom, and the relevant networking journals.
- Cross-domain work may activate multiple groups when the topic genuinely spans them.

Interpret wording precisely:

- `优先`, `重点`, `主要在这些 venue` means soft priority: search them first, then expand if useful.
- `只搜索`, `仅限`, `限定在这些 venue` means a hard filter: exclude other venues and disclose that coverage is intentionally restricted.
- `所有论文` for an author means collect the author's full high-coverage set; mark and sort preferred-venue papers first, but do not discard verified papers from other venues unless the user also says `仅限`.
- An explicit user-provided venue list always overrides the bundled default profile.

## Search by author

Read [references/author-search.md](references/author-search.md) for every author-based request. Never equate a name string with a unique person. Build and report an identity profile before claiming that publications belong to the same author.

### Mode 1: Author name

Use when the user supplies only a name.

1. Generate exact, reordered, abbreviated, transliterated, and known publishing-name variants without broadening to unrelated names.
2. Search author indexes and publication records for candidate identities.
3. Cluster results using stable author IDs, ORCID, topics, coauthors, institutions, email domains, and chronology.
4. If multiple plausible identities remain and choosing one would materially change the result, show the candidates and ask the user to select. Otherwise proceed with the best-supported identity and state confidence.
5. Keep ambiguous papers separate; do not silently assign them.

### Mode 2: Author name plus organization

Use the organization as identity evidence and a temporal filter, not as proof by itself.

1. Normalize the institution name, aliases, parent organization, laboratory, department, and historical names.
2. Determine whether the user means papers authored while affiliated with that organization or all papers by the person identified through that organization. State the interpretation; ask only if the distinction changes the requested result materially.
3. Verify affiliation at the paper level when applying a strict organization filter. Do not assume an author's current profile affiliation applies to older papers.
4. Retain former and later affiliations in the identity timeline when they help distinguish homonyms.

### Mode 3: Expand from a known paper

Use when the user supplies a title, DOI, URL, citation, or local PDF.

1. Resolve the seed paper against an authoritative record.
2. Extract the complete author list and preserve author order. Identify first, corresponding, last, or user-named authors only when the source establishes those roles; do not infer corresponding authorship from order.
3. Ask which author to expand only when the user has not specified one and the request cannot reasonably imply the target.
4. Anchor the author identity with the seed paper, then collect the author's publications using stable IDs and cross-source searches.
5. Separate confirmed, probable, and ambiguous records. Deduplicate preprints and published versions.

For requests phrased as "all papers," return a **high-coverage, identity-resolved publication set** unless a closed authoritative profile is proven complete. Search multiple complementary sources, paginate through full author profiles where supported, inspect result totals and boundary years, and report database coverage, retrieval date, and unresolved gaps.

Use only the identity labels `confirmed`, `probable`, `ambiguous`, and `excluded` defined in the reference. Do not introduce substitute labels such as `strong` or merge `probable` records into the confirmed main set.

## Search in passes

Use live web search or available scholarly connectors because paper indexes and citation data change. Never rely solely on memory.

### Minimize network approval interruptions

- Prefer the built-in web search, page-opening, browser, scholarly connector, or other read-only remote tool for webpages, DOI records, publisher pages, repository pages, and public APIs. Use these tools directly without asking the user for conversational permission unless the platform itself requires approval.
- Do not use shell commands such as `curl`, `wget`, `Invoke-WebRequest`, or ad hoc scripts when an available web or connector tool can retrieve the same public information.
- Batch independent searches, page opens, DOI lookups, and repository checks into as few tool calls as practical. Reuse results already obtained in the current task and do not repeat equivalent network requests.
- When a built-in web tool cannot access a required public endpoint, collect all remaining read-only endpoints first and make one narrowly scoped batch request through the fallback tool. Trigger an approval prompt only when enforced by the runtime; do not ask separately in chat and do not request approval endpoint by endpoint.
- An approval granted for one command or tool does not authorize bypassing later platform restrictions. Never claim that this skill can disable or override system, sandbox, credential, or network policies.
- If the user explicitly forbids network access, stop live browsing and clearly label the resulting coverage limitations.

1. Run a discovery pass across at least two complementary scholarly sources when available.
2. Run a precision pass using title phrases, authors, DOI, or repository identifiers.
3. Run citation chaining for seminal or survey papers when the request needs coverage rather than a quick sample.
4. Stop when the requested count is met and new searches mostly return duplicates or out-of-scope records.

Prefer first-party records such as publisher pages, DOI records, institutional repositories, arXiv, PubMed, ACL Anthology, or venue proceedings. Use aggregator records for discovery, not as the sole evidence when a primary record is available.

Do not claim the result is exhaustive unless the user supplied a closed database and a reproducible query that was fully evaluated. Say "high-coverage set" or "representative set" when appropriate.

## Screen and verify

Apply the declared inclusion and exclusion rules consistently. For every retained paper, verify as many of these fields as the task requires:

- Exact title
- Author list
- Publication year
- Venue or repository
- DOI or stable identifier
- Abstract or stated contribution
- Open-access or publisher URL

Open the paper landing page or authoritative record before describing its contribution. Do not infer findings from the title alone. Mark unavailable or uncertain metadata explicitly.

Deduplicate in this order:

1. DOI or canonical identifier
2. Normalized title plus first author and year
3. Preprint and published-version relationship

Prefer the peer-reviewed version as the main record and link the accessible preprint as a secondary URL when useful. Do not count both as separate papers unless the user requests version history.

## Separate online search from full-text enrichment

Treat ordinary web or scholarly-database searching as an online bibliographic workflow. In this workflow, verify titles, authors, affiliations, venues, years, abstracts, and stable source links, but do not promise reliable extraction of code repositories or experimental datasets from landing pages alone.

- Do not include code, code-status, dataset, or dataset-address columns in the default online-search Excel.
- Do not infer code or datasets from similar papers, citations, task conventions, or search snippets.
- Inspect code and dataset information only when the user explicitly requests it and a formal full text, supplementary material, official project page, or downloaded PDF is available.
- Route downloaded-paper code screening through the local PDF audit workflow below. Keep its report separate from the default bibliographic Excel unless the user explicitly asks to merge them.

## Audit downloaded PDFs for code links

Use this workflow when the user provides a local directory of downloaded papers and wants to retain only papers that provide code.

1. Resolve the exact input directory and enumerate PDF files before taking action.
2. Read [references/local-pdf-screening.md](references/local-pdf-screening.md) to choose strict or contextual matching and apply the safety rules.
3. Run `scripts/audit_code_links.py` in report mode first. Use the bundled PDF Python runtime when available.
4. Review every `needs_review` record and inspect borderline `no_code` records. Extracted text is a triage signal, not proof that the paper lacks a link.
5. Verify candidate links online when the user requires working code rather than merely a printed address.
6. Present the audit summary and report path before changing files.
7. Prefer quarantine. Apply a reviewed CSV report with the script's quarantine mode so files remain recoverable.
8. Delete permanently only when the user explicitly requests permanent deletion in the current task, the report has been reviewed, and the script's deletion confirmation token is supplied. Never delete `needs_review` records automatically.

Example report command:

```powershell
python scripts/audit_code_links.py "C:\papers" --output "C:\papers\code-link-audit.csv"
```

Example quarantine command after reviewing the report:

```powershell
python scripts/audit_code_links.py "C:\papers" --action quarantine --from-report "C:\papers\code-link-audit.csv" --confirm REVIEWED_NO_CODE_REPORT
```

Treat a repository URL printed in the PDF text or embedded as a PDF link annotation as strong evidence. Treat a general project page as code evidence only when nearby language explicitly identifies source code, an implementation, or a repository. Do not count DOI, dataset-only, model-weight-only, author-homepage, or generic lab URLs as code by default.

## Rank and organize

Rank papers according to the user's stated goal. If none is given, prioritize:

1. Direct relevance to the topic or keyword
2. Resolved author identity and scope compliance
3. Membership in the requested or bundled priority-venue profile
4. Evidentiary importance or influence within the field
5. Recency, when the request emphasizes current work
6. Metadata confidence and source quality

Group a broad collection by themes, methods, applications, chronology, or foundational versus recent work. Explain the grouping rule briefly. Distinguish literal keyword matches from semantic matches.

## Deliver the result

Lead with the scope, query interpretation, and number of retained papers. Use a compact table by default with:

| Paper | Year | Venue | Match reason | Contribution | Identifier/link |
|---|---:|---|---|---|---|

Keep contribution summaries short and evidence-based. Link titles to primary pages when possible. Include DOI as `https://doi.org/...` when verified.

After the table, provide:

- Search coverage: sources, date searched, principal queries, and filters
- Selection notes: inclusion, exclusion, ranking, and deduplication decisions
- Gaps or uncertainties: inaccessible abstracts, ambiguous versions, or likely coverage limitations

When the user requests machine-readable output, produce CSV, TSV, JSON, BibTeX, RIS, or Markdown using verified metadata. Do not invent missing BibTeX fields. Preserve Unicode author names and titles.

### Offer an Excel workbook after a paper search

After completing and presenting a paper search, ask one concise closing question unless the user has already accepted or declined spreadsheet output:

> 是否需要我把结果整理成 Excel？默认包含论文题目、作者、作者单位、期刊/会议、英文摘要、中文翻译、年份和来源链接；作者检索会把身份判定放在最后一列。

Do not ask this before searching, and do not repeat it in later turns after the user has answered. If the user agrees, create the workbook in the next step without asking for the default columns again. Read [references/excel-export.md](references/excel-export.md) and use the available spreadsheet skill for workbook creation and verification.

## Quality checks

Before finalizing:

- Confirm every listed paper has a working authoritative or stable link.
- Confirm titles, years, venues, and identifiers agree across sources or note discrepancies.
- Confirm every result satisfies the scope or is clearly labeled as adjacent.
- Confirm preprint and published versions are not double-counted.
- Confirm summaries do not overstate claims beyond the abstract or paper.
- Confirm any exported English abstract is copied from an authoritative or clearly identified source and its Chinese translation does not add claims absent from the original.
- Confirm exported author order, author roles, and author-affiliation mappings come from the paper or another authoritative record; never infer corresponding authorship from author order.
- When full-text enrichment is explicitly requested, confirm every exported code URL resolves to an implementation explicitly associated with that paper; do not substitute dataset, model-weight-only, author-homepage, or generic project URLs.
- When full-text enrichment is explicitly requested, confirm dataset names, roles, versions, and links are stated by the paper or an authoritative dataset source; do not infer datasets from the task or reuse a related paper's setup.
- Confirm the answer reports the search date for requests involving "latest" or recent work.
- Confirm local PDF cleanup never classifies unreadable, encrypted, scanned, or extraction-poor files as safe to delete.
- Confirm any moved or deleted PDF still matches the reviewed report's recorded size and modification timestamp.
- Confirm every author-based result is assigned to a resolved identity or labeled probable or ambiguous.
- Confirm organization filters use paper-time affiliation when strict affiliation is requested.
- Confirm "all papers" claims include source coverage, retrieval date, pagination or result-total checks, and unresolved uncertainty.
