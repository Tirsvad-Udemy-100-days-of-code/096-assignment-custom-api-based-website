# MIL-001 Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-22 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [9ebd5b7] |
| 2026-11-22 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-004 (stand-in for S01, not independent) | [9ebd5b7] |

---

## Purpose

Decide whether the repository baseline is ready for code.

## Deliverable

Repository with `pyproject.toml`, `.gitignore`, `constants.py`, `.editorconfig`, Doxyfile, git hooks, description and topics on the host, and the documented `.venv` setup.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` requires Python 3.14 or newer and lists Flask as the only runtime dependency | Met | Not met |
| 2 | `.gitignore` for Python exists and ignores `.venv` and `.env` | Met | Not met |
| 3 | `bash framework/scripts/check-editorconfig.sh` passes | Met | Not met |
| 4 | `doxygen Doxyfile` runs without errors | Met | Not met |
| 5 | Repository description and topics are set on the git host | Met | Not met |
| 6 | opengrep run reports no open findings | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First milestone |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2, Success Criteria 2, 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-22: within the Business Case constraint (plan ends 2026-11-29).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml and package skeleton | Python 3.14 or newer, Flask runtime dependency, pytest as development dependency, `src/` layout with `constants.py`. | No | |
| 2 | Add Python .gitignore and .editorconfig | Ignore `.venv`, `.env`, caches and build output; baseline `.editorconfig` from the framework. | No | |
| 3 | Add Doxyfile | Doxygen configuration for `src/`, output outside version control. | No | |
| 4 | Document the local .venv and pip upgrade | Commands to create the `.venv`, activate it, run `python -m pip install --upgrade pip` and install the project. | No | |
| 5 | Set repository description and topics | Set them through the git host API, with the token read from `.env` by hand and never by project code. | No | |
| 6 | Install git hooks and the local opengrep run | Enable the framework hooks and document the opengrep command used before each push. | No | |

---

[BC-001]: ../business-case.md
[9ebd5b7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/commit/9ebd5b70bcdc84dd3c9c0717dfb3daa949a76ed5
