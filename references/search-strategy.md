# Search Strategy Reference

## Source routing

Choose sources by domain and use at least one authoritative metadata source for verification.

| Need | Good discovery sources | Preferred verification sources |
|---|---|---|
| Cross-disciplinary | OpenAlex, Semantic Scholar, Google Scholar search results | Crossref, DOI landing page, publisher or repository page |
| Computer science | DBLP, Semantic Scholar, arXiv | DBLP, ACM/IEEE proceedings, ACL Anthology, arXiv record |
| Biomedicine | PubMed, Europe PMC | PubMed, journal page, ClinicalTrials.gov when relevant |
| Physics and mathematics | arXiv, INSPIRE for high-energy physics | arXiv, journal or DOI page |
| Social sciences and humanities | OpenAlex, discipline indexes, library catalogs | Publisher, journal, DOI, or institutional repository |

Avoid treating ordinary web pages, generated reading lists, or search snippets as final metadata evidence.

For communications, networking, wireless, multimedia, image/video, computer vision, AI, machine learning, data mining, web, and computer-systems searches, load [priority-venues.md](priority-venues.md). Select only the topical venue groups relevant to the query, then run a venue-priority pass before broad discovery unless the user supplies a different venue list or explicitly disables venue prioritization.

## Query patterns

Use combinations appropriate to the index:

- Exact phrase: `"target phrase"`
- Synonyms: `("term A" OR "term B" OR abbreviation)`
- Intersection: `concept AND method AND application`
- Title focus: `intitle:"target phrase"` when supported
- Site focus: `site:arxiv.org`, `site:pubmed.ncbi.nlm.nih.gov`, or a venue domain
- Venue focus: combine the concept with the venue's canonical title and one unambiguous alias, or use the database's publication-title/venue filter
- Time focus: add the year range through database filters when possible
- Exclusion: add `-term` only for repeated, well-understood false positives

For Chinese topics, search both Chinese and English translations. Keep technical names, dataset names, and model names untranslated when they are normally published in English.

## Search modes

### Direction discovery

Start with a recent survey, review, benchmark, or tutorial to identify terminology and clusters. Search each cluster separately, then add foundational and recent representative work. Use backward and forward citation chaining where supported.

### Keyword containment

Define the matching field before reporting counts:

1. Title contains the exact keyword
2. Title or abstract contains the exact keyword
3. Metadata keywords contain it
4. Paper is semantically related but does not contain it

Do not merge these categories silently. Search interfaces often index different fields, so report the field and source used.

### Latest papers

Use an explicit date boundary and record the search date. Sort by publication or submission date, then verify that online-first dates, conference dates, and preprint revision dates are not being conflated.

### Seminal papers

Use citation counts only as one signal because counts vary by source and favor older work. Combine citations with surveys, field histories, venue reputation, and direct relevance. Name the citation source and retrieval date if reporting a count.

## Metadata conflict rules

Resolve conflicts in this order:

1. Published article or proceedings page
2. DOI registration record
3. Curated domain index
4. Institutional or preprint repository
5. General scholarly aggregator

Keep the conference year distinct from the online-publication year when both matter. Preserve the published title's punctuation and capitalization unless the requested citation style requires normalization.

## Coverage heuristics

For a quick list, use two complementary sources and verify each retained item. For a literature review, add query variants, citation chaining, and venue-specific searches. For a systematic or scoping review, do not imply compliance with PRISMA or another protocol unless the full protocol, databases, dates, exact query strings, screening stages, and exclusion reasons are documented.
