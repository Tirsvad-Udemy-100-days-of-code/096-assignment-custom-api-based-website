# MIL-003 Flask website

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-22 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [9ebd5b7] |
| 2026-11-22 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-006 (stand-in for S01, not independent) | [9ebd5b7] |

---

## Purpose

Decide whether the website shows the API data correctly.

## Deliverable

A Flask application with a character list, a house filter, a character page and an error page, tested with the Flask test client.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /` lists characters | Met | Not met |
| 2 | `GET /house/<name>` filters by house | Met | Not met |
| 3 | `GET /character/<id>` shows one character, 404 when unknown | Met | Not met |
| 4 | An unavailable API shows an error page with status 503 | Met | Not met |
| 5 | `pytest` passes | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The site consumes the client |

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

2026-11-24: within the Business Case constraint (plan ends 2026-11-29).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create the Flask application factory and routes | Controllers call the client port; routes and messages come from `constants.py`. | No | |
| 2 | Add templates and static styles | List, house, character and error templates; no JavaScript framework. | No | |
| 3 | Write route tests | Flask test client with a fake client for success, 404 and 503. | No | |
| 4 | Add the run entry point | `python -m` command that starts the site locally. | No | |

---

[BC-001]: ../business-case.md
[9ebd5b7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/commit/9ebd5b70bcdc84dd3c9c0717dfb3daa949a76ed5
