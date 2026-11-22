# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-005], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-22 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-005]
- Checklist used: [QC-WIKI-001]
- Scope: full review of docs/wiki/
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | Checked against the document: met. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Checked against the document: met. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Checked against the document: met. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | Checked against the document: met. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Checked against the document: met. |
| 6 | The sidebar does not repeat the page list per language | Pass | Checked against the document: met. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | Pass | Checked against the document: met. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Checked against the document: met. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | Checked against the document: met. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 22 files: 7 pages plus the sidebar; en, da and ms have the same 7 pages. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Checked against the document: met. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Checked against the document: met. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Checked against the document: met. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | Cannot be checked before the merge; the published wiki is checked after it (action item). |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | Pass | Checked against the document: met. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All files sit directly in docs/wiki/. |

## Overall Verdict

Go for the merge — every Mandatory criterion passes except criterion 14, which can only be checked on the published wiki after the merge (see the action item).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the sidebar, every page and every link on the published wiki after the merge (criterion 14) | S01 | 2026-11-22 |

---

[MIL-005]: ../../milestones/mil-005-wiki.md
