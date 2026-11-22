# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-22 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [9ebd5b7] |
| 2026-11-22 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-002 (stand-in for S01, not independent) | [9ebd5b7] |

---

## Purpose

Identify who the project serves and what each needs, using a power/interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Course participant | Product Owner, developer, reviewer | Self | HIGH | HIGH | Manage Closely | Finish the assignment with a clean, reviewed result |
| S02 | Udemy coursists | Peers | Course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and run instructions |
| S03 | GitHub viewers | Browsers of the repository | Public | LOW | MEDIUM | Keep Informed | Clear description, topics and README, and no runtime dependencies beyond Flask |

## Power/Interest Classification Rationale

S01 decides scope and accepts every artifact, so power and interest are high. S02 and S03 cannot change the project but read its output.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Working site that uses the API | Functionality |
| CN-002 | S02 | Code that is easy to read and run | Usability |
| CN-003 | S02 | Assignment function names kept | Functionality |
| CN-004 | S03 | Clear repository description and topics | Usability |
| CN-005 | S03 | Few dependencies | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| COM-001 | Pull request | Per milestone | Reviewed change | All |
| COM-002 | README and wiki | Once | Run instructions, screenshots, lessons | MIL-004, MIL-005 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Rich features against few dependencies | S01, S03 | Standard library for HTTP; Flask only |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objective 1 |
| S02 | CN-002, CN-003 | Objectives 2, 3 |
| S03 | CN-004, CN-005 | Objectives 3, 4 |

## Sign-Off

S01 accepts this analysis.

---

[BC-001]: ./business-case.md
[9ebd5b7]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/commit/9ebd5b70bcdc84dd3c9c0717dfb3daa949a76ed5
