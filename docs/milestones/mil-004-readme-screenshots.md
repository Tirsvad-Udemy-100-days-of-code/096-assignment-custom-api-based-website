# MIL-004 README and screenshots

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-22 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-22 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-007 (stand-in for S01, not independent) | pending |

---

## Purpose

Decide whether a reader can run the project from the README.

## Deliverable

README from the framework template with run and test instructions and a screenshot for each lecture step.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README follows the framework template and `check-readme.sh` passes | Met | Not met |
| 2 | README documents `.venv`, pip upgrade, run and test commands | Met | Not met |
| 3 | A screenshot exists for every lecture step and is shown in README | Met | Not met |
| 4 | Screenshots were taken in a Docker container, not on the host desktop | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Needs the running site |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3, 4; Success Criteria 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-25: within the Business Case constraint (plan ends 2026-11-29).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write README from the framework template | Describe the project, requirements, setup, run, tests and Doxygen. | No | |
| 2 | Capture a screenshot per lecture step | Choose API, first request, house filter, character page, error page; taken in a Docker container with a headless browser. | No | |
| 3 | Embed screenshots in README | Store images under `docs/images/` and reference them. | No | |

---

[BC-001]: ../business-case.md
