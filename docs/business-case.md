# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-22 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | pending |
| 2026-11-22 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-009 (stand-in for S01, not independent) | pending |

---

## Executive Summary

Build a small Flask website that shows data from a public Harry Potter REST API (characters, houses, spells). The project is the Day 96 assignment of a Python course and is published as a readable, runnable example for other course participants. Recommendation: proceed.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`, ISO/IEC 25010:2023 quality characteristics for review criteria, and the conventions of the `coding-conventions` skill (Python).

## Problem Statement

The assignment asks for a website built on an interesting public API, applying HTTP requests and REST knowledge. Belief that would kill the idea if false: a free public Harry Potter API is reachable and returns stable JSON. The original API named in the lecture is no longer maintained, so a working replacement must be chosen and the client must fail gracefully when the API is down.

## Business Opportunity

Course participants compare solutions; a clean, tested and documented solution is a reference for them and for repository visitors.

## Objectives

1. Deliver a Flask website that lists characters, filters by house and shows one character.
2. Keep the code readable, tested with pytest and documented with Doxygen comments.
3. Document how to create a local `.venv`, run the site and run the tests.
4. Provide a README and a wiki in English, Danish and Bahasa Malaysia with a screenshot for each lecture step.

## Scope

### In Scope

- Flask website, API client, constants, tests, Doxygen configuration.
- Repository description and topics on the git host.
- README from the framework template, and a three-language wiki with screenshots.
- A local static analysis run before each push.

### Out of Scope

- User accounts, a database, deployment to a hosting service.
- Runtime dependencies other than Flask.

## Expected Benefits

### Tangible Benefits

- A working, tested example that runs with three commands.

### Intangible Benefits

- Practice with REST APIs, Flask and the plan-first workflow.

## Strategic Alignment

Supports the course goal of building one project per day and the repository goal of a browsable collection of reviewed solutions.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass | 100 % | `pytest` exit code 0 |
| 2 | Runtime dependencies | 1 (Flask) | `pyproject.toml` |
| 3 | Wiki languages | 3 (en, da, ms) | files under `docs/wiki/` |
| 4 | Screenshot per lecture step | all steps | images referenced in README and wiki |
| 5 | Static analysis findings | 0 open | local run before push |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Public API is offline or changes | Site shows no data | Client returns a clear error; tests use a fake client |
| Python 3.14 not installed on a reader's machine | Cannot run | README states the requirement and how to check it |
| Token leaked | Account misuse | Tokens stay in `.env`, which is ignored and never read by the project |

## Assumptions

- The Product Owner, developer and reviewer is S01; the people the project is for (S02, S03) are reached only through the repository.
- PO language is English, domain is IT; the stage is a prototype.
- The presentation pattern is MVC (website), with Flask views as controllers.
- The `.env` file is for personal use only and is not imported, read or tested by the project.

## Constraints

- Python 3.14 or newer, a local `venv`, `pytest`, `pyproject.toml`, `constants.py` for constants.
- Folder structure `src/`, `tests/`, `docs/`.
- No mention of the tooling that assisted the work in any artifact.
- One branch and pull request per milestone.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About two hours of work, no licences | A reusable reference solution |

The assessment is qualitative on purpose: this is a no-revenue course assignment, so a money figure would carry no information.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; completes the assignment |
| S02 | Course participants; want readable, runnable code and run instructions |
| S03 | Repository viewers; want a clear description, topics and README |

## Recommendation

Proceed — low cost, clear scope and one small dependency.
