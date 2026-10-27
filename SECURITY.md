# Security policy

do-it-clean is a security tool, so problems with it matter. Thank you for reporting them privately.

## How to report
Use GitHub's private reporting: open this repo's **Security** tab and click **Report a vulnerability**. Only the maintainer can see your report.

Please **don't** open a public issue, pull request, or discussion about a security problem until it's fixed.

## What to include
- What the problem is, and what an attacker could do with it.
- Steps to reproduce it. A small example repo or instruction file is ideal.
- The do-it-clean commit you used, and your Claude Code version (`claude --version`).

Don't include real secrets or anyone's private data. Fake values work fine.

## What to expect
This project is maintained by one person, on a best-effort basis.
- I aim to reply within **7 days**.
- I'll tell you whether I can reproduce the problem, and keep you updated while it's being fixed.
- Once it's fixed, I'll credit you in the fix notes, unless you'd rather stay anonymous.

There's no bug bounty.

## What counts
**In scope:**
- Getting past the lockdown, for example running a command, fetching a site outside the allowlist, or reading or writing outside the allowed folders.
- An audited repo causing any of the above, or causing do-it-clean to leak data (for example, putting a secret into a report).
- An audited repo hiding a problem from the report, or getting do-it-clean to recommend something harmful.
- A flaw in the test (`test/`) that would let one of the above pass unnoticed.

**Out of scope:**
- The fake secrets and attacks in `fixtures/`. They're deliberate test data.
- Problems in Claude Code itself, or in the AI model. Report those to Anthropic.
- The fact that files the audit reads are sent to Anthropic for processing. The README says so; it's how Claude Code works.
- Findings the audit simply misses, with no security impact. Open a normal issue for those.

## Supported versions
Only the latest version on the `main` branch.

## Good faith
If you research and report in good faith, without harming others, accessing data that isn't yours, or disrupting services, I won't take action against you, and I'll work with you to understand and fix the problem.
