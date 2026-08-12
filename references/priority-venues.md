# Priority Venues for Communications and Computing

Use this profile by default for communications, networking, wireless, multimedia, image/video, computer vision, AI, machine learning, data mining, web, and computer-systems searches when the user does not provide a different venue policy.

## Interpretation

- Treat this as a search and ranking priority, not an automatic inclusion requirement.
- Search priority venues first, then run a broader discovery pass unless the user says `只搜索`, `仅限`, or equivalent.
- For an author's `所有论文`, retain verified papers from all venues and place profile matches first. Apply a strict exclusion only when `所有论文` is combined with an explicit venue-only instruction.
- Prefer exact venue fields in IEEE Xplore, ACM Digital Library, DBLP, Crossref, OpenAlex, or Semantic Scholar. A web query that merely contains an abbreviation is not venue proof.
- Verify the final venue from the publisher, proceedings, DOI record, or curated domain index. Do not assign a venue from a search snippet alone.
- Activate only venue groups relevant to the request. Do not query vision, machine-learning, data-mining, and systems venues indiscriminately for an unrelated communications topic.

## Priority journals

| Canonical venue | Search aliases |
|---|---|
| IEEE Journal on Selected Areas in Communications | IEEE JSAC; JSAC |
| IEEE Transactions on Wireless Communications | IEEE TWC; TWC |
| IEEE Transactions on Communications | IEEE TCOM; TCOM |
| IEEE Communications Surveys & Tutorials | IEEE ComST; IEEE CST; Communications Surveys & Tutorials |
| IEEE/ACM Transactions on Networking | IEEE/ACM ToN; IEEE/ACM TON; Transactions on Networking |
| IEEE Transactions on Mobile Computing | IEEE TMC; TMC |
| IEEE Internet of Things Journal | IEEE IoT Journal; IEEE IoT-J; IoT Journal |
| IEEE Transactions on Network and Service Management | IEEE TNSM; TNSM |
| IEEE Communications Letters | IEEE CL; Communications Letters |
| IEEE Wireless Communications Letters | IEEE WCL; Wireless Communications Letters |
| IEEE Transactions on Multimedia | IEEE TMM; TMM |
| IEEE Transactions on Circuits and Systems for Video Technology | IEEE TCSVT; TCSVT |
| IEEE Transactions on Image Processing | IEEE TIP; TIP |
| IEEE Transactions on Signal Processing | IEEE TSP; TSP |
| IEEE Signal Processing Letters | IEEE SPL; SPL |

## Communications, networking, multimedia, and signal-processing conferences

| Canonical venue | Search aliases and series notes |
|---|---|
| IEEE Global Communications Conference | IEEE GLOBECOM; GLOBECOM |
| IEEE International Conference on Communications | IEEE ICC; ICC |
| IEEE Conference on Computer Communications | IEEE INFOCOM; INFOCOM |
| ACM SIGCOMM Conference | ACM SIGCOMM; SIGCOMM |
| ACM International Conference on Mobile Computing and Networking | ACM MobiCom; MobiCom |
| IEEE Wireless Communications and Networking Conference | IEEE WCNC; WCNC |
| IEEE International Symposium on Personal, Indoor and Mobile Radio Communications | IEEE PIMRC; PIMRC |
| IEEE Vehicular Technology Conference | IEEE VTC; VTC Spring; VTC Fall; VTC-Spring; VTC-Fall |
| IEEE International Conference on Multimedia and Expo | IEEE ICME; ICME |
| IEEE International Conference on Image Processing | IEEE ICIP; ICIP |
| IEEE International Conference on Acoustics, Speech and Signal Processing | IEEE ICASSP; ICASSP |
| ACM Multimedia Systems Conference | ACM MMSys; MMSys; ACM Multimedia Systems |

## Computer vision conferences

| Canonical venue | Search aliases and series notes |
|---|---|
| IEEE/CVF Conference on Computer Vision and Pattern Recognition | CVPR; IEEE CVPR; IEEE/CVF CVPR |
| IEEE/CVF International Conference on Computer Vision | ICCV; IEEE ICCV; IEEE/CVF ICCV |
| European Conference on Computer Vision | ECCV; European Conference on Computer Vision |
| IEEE/CVF Winter Conference on Applications of Computer Vision | WACV; IEEE WACV; IEEE/CVF WACV |

## Artificial intelligence and machine-learning conferences

| Canonical venue | Search aliases and series notes |
|---|---|
| Conference on Neural Information Processing Systems | NeurIPS; NIPS (historical alias) |
| International Conference on Machine Learning | ICML |
| International Conference on Learning Representations | ICLR |
| AAAI Conference on Artificial Intelligence | AAAI; AAAI Conference |
| International Joint Conference on Artificial Intelligence | IJCAI |

## Multimedia, data-mining, and web conferences

| Canonical venue | Search aliases and series notes |
|---|---|
| ACM International Conference on Multimedia | ACM Multimedia; ACM MM; MM |
| ACM SIGKDD Conference on Knowledge Discovery and Data Mining | ACM KDD; KDD; SIGKDD |
| ACM Web Conference | The Web Conference; WWW; ACM WWW; WebConf |

## Computer-systems conferences

| Canonical venue | Search aliases and series notes |
|---|---|
| USENIX Symposium on Networked Systems Design and Implementation | NSDI; USENIX NSDI |
| USENIX Symposium on Operating Systems Design and Implementation | OSDI; USENIX OSDI |
| ACM Symposium on Operating Systems Principles | SOSP; ACM SOSP |
| European Conference on Computer Systems | EuroSys; ACM EuroSys |
| USENIX Annual Technical Conference | USENIX ATC; ATC |

## Search sequence

1. Build concept and author queries without venue restrictions.
2. Select the topical groups that match the request. Run venue-filtered searches across those groups, batching related venues where the source supports an OR filter.
3. Verify exact venue membership and label matches as `priority venue` internally.
4. Run a broad, venue-unrestricted pass to find omissions and non-profile work.
5. Deduplicate by DOI or canonical identifier, then title/first-author/year.
6. Sort by relevance and identity confidence first, priority-venue membership next, then the user's recency or influence preference.
7. Report profile coverage: venues searched, date, any source limitations, and the number of retained profile versus non-profile papers.

## Query examples

Soft priority:

```text
"cross-modal semantic communication" AND ("IEEE Journal on Selected Areas in Communications" OR "IEEE Transactions on Wireless Communications")
```

Author within the profile:

```text
author:"Hengfa Liu" AND ("IEEE Internet of Things Journal" OR "IEEE Transactions on Multimedia")
```

Use source-specific structured venue filters when available instead of relying only on these free-text forms.
