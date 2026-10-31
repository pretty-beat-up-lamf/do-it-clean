# Model notes

Model-specific claims, such as "model X no longer needs Y spelled out". **Each one is a hypothesis, not a fact.**

## Staleness rule
An entry is **stale** when either is true:
- `verified` is more than 60 days old, or
- a newer model in the same family has shipped since `verified`.

Audits must not rely on stale entries. The self-audit proposes a recheck for each one (confirm, revise, or delete) and cites its sources.

## Entries

Starts empty on purpose. The self-audit adds entries only when it can cite a source.

| Claim | Applies to | Source | Verified (YYYY-MM-DD) | Status |
|---|---|---|---|---|
| On a repo with many planted attacks, a safety classifier can stop the report from being saved, even when the report describes attacks without quoting them. Use the default model for attack-heavy repos. | claude-sonnet-5-5 | `reports/test-results-claude-sonnet-5-5-2026-10-30-harbor-notes.md` (blocked by a safety classifier, from the run log, after the no-quoting rule); `reports/test-results-sonnet-harbor-notes.md` (2 earlier runs, no report saved) | 2026-10-30 | Current |
