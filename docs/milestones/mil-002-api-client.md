# MIL-002 API client

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-22 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-22 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-005 (stand-in for S01, not independent) | pending |

---

## Purpose

Decide whether the data layer is reliable enough to build the website on.

## Deliverable

A tested client for a maintained public Harry Potter API, behind a port, with fixture-based tests and an ADR naming the chosen API.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | An ADR records the chosen API and why the lecture's API was replaced | Met | Not met |
| 2 | The client returns characters, filtered by house, and one character by id | Met | Not met |
| 3 | Network failure raises a domain error, covered by a test | Met | Not met |
| 4 | `pytest` passes without network access | Met | Not met |
| 5 | All source has Doxygen comments | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Tooling and layout must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1, 2; Success Criteria 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-23: within the Business Case constraint (plan ends 2026-11-29).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write ADR for the API choice | Compare maintained Harry Potter APIs, record the decision and the retired original. | No | |
| 2 | Define character model and client port | Domain dataclass and an abstract client the website depends on. | No | |
| 3 | Implement the HTTP client with the standard library | Use `urllib`; endpoints and timeouts come from `constants.py`. | No | |
| 4 | Write client tests with fixtures | Parsing, house filter, not found and network error, with no live calls. | No | |

---

[BC-001]: ../business-case.md
