# Excel Export for Paper Collections

Use this workflow after the user accepts the post-search Excel offer or directly requests an `.xlsx` paper list.

## Default columns

Create one row per deduplicated paper with these columns in this order:

1. `论文题目`
2. `作者`
3. `作者单位`
4. `期刊/会议`
5. `英文摘要`
6. `中文摘要翻译`
7. `年份`
8. `来源链接`
9. `核验备注`
10. `身份判定` — include for author-based searches and always place it last

Do not add separate `第一作者` or `通讯作者` columns. Do not add separate `卷号/期号/页码`, `DOI/稳定标识`, `使用数据集`, `数据集地址/获取方式`, `代码地址`, or `代码状态` columns by default. Add any of these only when the user explicitly requests them after seeing the streamlined schema.

Use the canonical published title. Put journal and conference names in the same `期刊/会议` column. Keep that cell to the venue name; do not append volume, issue, or page numbers. Use the best authoritative landing page as `来源链接`; a DOI URL may serve as the source link without creating a separate DOI column.

If optional columns are explicitly requested, insert them before `身份判定`, which must remain the final column.

## Authors, roles, and affiliations

- Preserve the complete published author list and its order. Prefer full publishing names; do not expand initials unless an authoritative source establishes the full name.
- Bold the first author and every explicitly identified corresponding author only within the `作者` cell. Bold all explicitly declared co-first or co-corresponding authors.
- Treat the first listed author as the first author unless the paper explicitly declares shared first authorship. Never infer corresponding authorship from author order.
- Verify corresponding-author and equal-contribution markers from the formal PDF, publisher page, or proceedings record. If corresponding authorship cannot be verified, do not guess; add `通讯作者未核实` to `核验备注`.
- Never create separate first-author or corresponding-author columns as a formatting fallback. If mixed rich-text bolding is unreliable, keep one ordered `作者` cell and add concise inline markers such as `【一作】` or `【通讯】` only for verified roles; disclose this fallback in the delivery note.
- Preserve author-affiliation mapping with numbered markers when the source provides it, for example `Mengqi Yuan¹; Gengyun Jia²` and `¹ Nanjing University...; ² Hefei University...`.
- Include every distinct affiliation printed for the authors, not only the target author's current organization. Do not apply a current profile affiliation retroactively.
- If the source lists affiliations without author-to-affiliation mapping, record the organizations and mark the mapping uncertain rather than assigning them to individuals.

## Abstract sourcing and translation

- Retrieve the abstract from the publisher, formal proceedings, DOI metadata, PubMed, arXiv, institutional repository, or another authoritative record.
- Preserve the complete English abstract when licensing and source-access constraints permit. Do not reconstruct an abstract from a title, introduction, search snippet, or contribution summary.
- If no reliable abstract is available, write `未获取到权威英文摘要` in `英文摘要`, leave the translation blank, and explain the gap in `核验备注`.
- Translate faithfully into natural academic Chinese. Preserve technical terms, model names, quantities, hedging, and claim strength. Do not add facts absent from the English abstract.
- When the available source is not English, keep the source-language abstract in an explicitly named optional column and do not label a machine-generated English version as the original abstract.
- Respect source quotation and copyright limits. When full abstract reproduction is not permitted, include a concise paraphrase, rename the column `英文摘要概述`, and translate that overview faithfully.

## Online-search boundary

For a normal online-only paper search, do not add dataset or code fields. Landing pages and bibliographic indexes often omit these details, so absence online is not evidence that the paper has no code or data release.

Collect code or dataset information only when the user explicitly requests full-text enrichment and one of these sources is available:

- Formal PDF or downloaded local paper
- Supplementary material or data/code availability statement
- Official project page or author-controlled repository clearly tied to the paper
- Official dataset documentation cited by the paper

When auditing downloaded PDFs for code links, use the skill's local PDF workflow and produce a separate audit report by default. Do not merge audit results into this workbook unless requested.

## Identity status

- Use only `confirmed`, `probable`, `ambiguous`, or `excluded` for author-disambiguation status.
- Include `身份判定` for author-based searches; omit it when identity resolution is irrelevant.
- Keep `身份判定` as the rightmost column, after all default and explicitly requested optional columns.

## Workbook layout

- Use the available spreadsheet skill and its required creation, formatting, rendering, and verification workflow.
- Name the main sheet `论文清单`.
- Freeze the header row, enable filters, wrap abstract columns, align long text to the top, and use readable widths without producing an excessively wide sheet.
- Apply mixed rich-text bolding to verified author roles when supported, and visually confirm it survives `.xlsx` export.
- Keep `来源链接` as a plain-text clickable URL.
- Use typed numeric values for years. Leave unknown metadata blank or mark it explicitly uncertain; never invent values.
- For more than 100 papers, keep one master sheet unless the user requests thematic or yearly sheets.

## Verification

- Confirm the workbook row count equals the final deduplicated paper count.
- Spot-check titles, author order, inline role emphasis, author-affiliation mappings, venue names, abstracts, translations, years, source URLs, notes, and identity labels against the verified collection.
- Confirm no default workbook contains separate first-author, corresponding-author, volume/issue/page, DOI, dataset, dataset-address, code-address, or code-status columns.
- Confirm `身份判定`, when present, is the last column.
- Scan for blank required fields, accidental duplicate rows, broken source URLs when verification is possible, and spreadsheet formula errors.
- Render and visually inspect every sheet before export.
