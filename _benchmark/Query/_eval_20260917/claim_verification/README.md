# ThermoML Q1 claim verification

The active material is now limited to [claim_verification](claim_verification/).
It contains one canonical JSON file per reviewed answer:

- 42 answers across seven benchmark groups
- 796 resolved claims
- 5 explicitly unresolved empirical assertions
- 392 database-verified, 298 domain-knowledge, and 106 incorrect claims

Start with [the claim manifest](claim_verification/manifest.json) or
[the package README](claim_verification/README.md). The manifest records every
answer-file hash, claim count, category count, original answer hash, and source
availability status.

The former aggregate inventories, CSV/Markdown renderings, whole-answer scores,
plots, resource statistics, scripts, and intermediate reviewer versions were
moved—not deleted—to [obsolete/legacy_full_comparison](obsolete/legacy_full_comparison/).
They are retained only for recovery and provenance and are not an active second
version of the claim review.
