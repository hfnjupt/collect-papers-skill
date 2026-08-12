# Author Search and Identity Resolution

## Identity evidence hierarchy

Prefer evidence in this order while recognizing that any source can be stale or incomplete:

1. ORCID linked from a publisher, institution, or author-controlled page
2. Stable domain author ID with matching seed publications, such as DBLP, PubMed, OpenAlex, Semantic Scholar, Scopus, or Web of Science identifiers when accessible
3. Official institutional profile or author-controlled publication page
4. Exact seed-paper match plus consistent coauthors, topics, affiliation, and chronology
5. Name and affiliation string alone

Require multiple independent signals for common names. Do not merge profiles merely because a scholarly index suggests a match.

## Name normalization

Search only plausible variants:

- Original script and Romanized form
- Given-name and family-name order
- Full given names and initials
- Hyphenation, spacing, diacritics, and punctuation variants
- Published aliases supported by a profile or publication record

For Chinese and other transliterated names, do not invent a mapping from initials or Romanization to a specific person without corroborating evidence. Preserve Unicode names in output.

## Organization normalization

Build a compact alias set covering:

- Official English and local-language names
- Common abbreviation
- Parent university, company, hospital, or research institute
- Laboratory and department when they are important for disambiguation
- Historical names, mergers, and renamed units when relevant to the publication years

Distinguish these two scopes:

- **Affiliation-bounded**: Include only papers whose author affiliation at publication matches the organization.
- **Identity-bounded**: Use the organization to identify the person, then include that person's publications across all affiliations.

Report which scope was used. If a paper does not expose author-affiliation mapping, label the affiliation uncertain rather than applying the current affiliation retroactively.

## Known-paper expansion

Resolve the seed paper using DOI, exact title, venue page, repository ID, or PDF metadata. Record:

- Canonical title and identifier
- Full ordered author list
- Author IDs linked by the source
- Affiliations mapped to individual authors, when available
- Corresponding-author markers only when explicitly shown

Use the seed paper as a strong identity anchor. Verify candidate profiles contain the seed paper or an unmistakable version of it. If multiple author profiles contain it because of duplicate indexing, merge records only after confirming other identity signals.

## High-coverage publication collection

Use at least two complementary sources when available. Prefer sources according to discipline and identity support:

| Source | Useful evidence | Common limitation |
|---|---|---|
| ORCID | Self-associated identity and works | Profiles may be incomplete or stale |
| DBLP | Curated CS author pages and name disambiguation | Limited outside computer science |
| PubMed | Biomedical records and affiliations | Author identity coverage varies |
| OpenAlex | Broad works, author and institution IDs | Profiles can be split or merged incorrectly |
| Semantic Scholar | Broad author profiles and topics | Profile assignment can be incomplete |
| Publisher or venue | Authoritative paper metadata | No complete cross-publisher bibliography |
| Institutional or personal page | Identity and selected works | Often selective rather than exhaustive |

When an API or profile paginates, retrieve all pages within the requested scope. Compare stated totals with collected unique records. Search for missing boundary years and known venues. Cross-check the oldest, newest, and seed publications. Do not use citation count as identity evidence.

## Confidence labels

Assign each paper one label:

- **Confirmed**: Stable identity linkage or multiple strong matching signals
- **Probable**: Strong topical, coauthor, affiliation, and chronological match but no stable linkage
- **Ambiguous**: One or more plausible homonymous authors remain
- **Excluded**: Evidence indicates another person

Default the main publication table to confirmed records. Put probable and ambiguous records in separate sections unless the user requests a broader set.

## Output for author searches

Start with an identity card:

| Field | Value |
|---|---|
| Canonical publishing name | ... |
| Name variants searched | ... |
| Current and historical organizations | ... |
| Stable IDs | ORCID, DBLP, OpenAlex, or others |
| Seed paper | ... |
| Identity confidence | High, medium, or unresolved |

Then present publications with an additional `Identity evidence` or `Confidence` column. For an affiliation-bounded search, include the paper-time affiliation. For a high-coverage set, report sources, exact retrieval date, source result totals when available, collected count before and after deduplication, excluded ambiguous count, and known coverage gaps.
