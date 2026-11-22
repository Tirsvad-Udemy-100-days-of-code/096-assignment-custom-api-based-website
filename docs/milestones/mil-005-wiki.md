# MIL-005 Wiki and reflection

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-22 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [9ebd5b7] |
| 2026-11-22 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-008 (stand-in for S01, not independent) | [9ebd5b7] |

---

## Purpose

Decide whether the wiki and reflection are complete.

## Deliverable

Wiki pages in English, Danish and Bahasa Malaysia, each explaining what each lecture step taught, with screenshots, and the reflection.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Wiki pages exist in en, da and ms and `check-languages.sh` passes | Met | Not met |
| 2 | Each page explains what was gained at each lecture step | Met | Not met |
| 3 | Each page shows the screenshot of each step | Met | Not met |
| 4 | The reflection answers the assignment's questions | Met | Not met |
| 5 | opengrep run reports no open findings before the final push | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | Reuses the screenshots |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4; Success Criteria 3, 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-26: within the Business Case constraint (plan ends 2026-11-29).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | Home plus one page per lecture step: what was gained, with screenshot. | No | |
| 2 | Write the Danish wiki | Same structure as English. | No | |
| 3 | Write the Bahasa Malaysia wiki | Same structure as English. | No | |
| 4 | Write the reflection | Approach, what was hard and easy, biggest learning, what to do differently. | No | |
| 5 | Final checks | Run pytest, Doxygen, opengrep and the framework checks. | No | |

---

[BC-001]: ../business-case.md
[9ebd5b7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/commit/9ebd5b70bcdc84dd3c9c0717dfb3daa949a76ed5
