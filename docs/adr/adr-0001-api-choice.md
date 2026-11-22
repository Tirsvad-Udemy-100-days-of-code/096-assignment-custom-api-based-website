# Architecture Decision Record

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-22 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [32c2177] |
| 2026-11-22 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-010 (stand-in for S01, not independent) | [32c2177] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The lecture names the Potter API at `potterapi.com`, which is retired. The project needs a free, key-less, read-only REST API that returns characters with their house. Constraints: no API key in the repository, JSON over HTTPS, stable field names. Options checked on 2026-11-22:

1. `hp-api.onrender.com`: the service answers "Service Suspended", so it is unusable.
2. PotterDB at `api.potterdb.com`: answers, but uses the JSON:API envelope and has no house filter on characters.
3. Potter API by fedeperin at `potterapi-fedeperin.vercel.app`: answers; plain JSON arrays with `fullName`, `nickname`, `hogwartsHouse`, `interpretedBy`, `children`, `image`, `birthdate` and `index`; also serves houses and spells.

## Decision

Use the Potter API by fedeperin (option 3), read the `en` language path, and keep its address in `constants.py`. The client sits behind a port, so another API can replace it without changing the website.

## Consequences

**Positive:**

- Plain JSON arrays are easy to parse with the standard library.
- No key and no extra runtime dependency.
- The port limits the cost of a later change of API.

**Negative:**

- A free hosted service can go offline, as the lecture's API did; the website shows an error page then.
- The API has no server-side house filter, so the client filters locally.

## Affected Artifacts

- [BC-001] — fulfils the objective of showing data from a public API and the risk "Public API is offline or changes".

---

[BC-001]: ../business-case.md
[32c2177]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/096-assignment-custom-api-based-website/commit/32c21773dbcb01ce83558dd4398d4bbdaae00875
