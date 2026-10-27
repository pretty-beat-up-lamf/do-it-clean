# Sources digest

Written by each run: the date of the last check, plus one line per source noting anything relevant that changed. The next run only reads what's newer than this date. Empty until the first run.

Last checked: 2026-10-27

## 2026-10-27 (first run, fixture target)
- memory: target under 200 lines per CLAUDE.md; imports don't reduce context cost. Claude Code reads AGENTS.md natively (v2.1.277+), but by default only when no CLAUDE.md / CLAUDE.local.md exists; `@AGENTS.md` import in CLAUDE.md loads both without double-reading.
- skills: SKILL.md under 500 lines; `description` should say what the skill does and when to use it (listing truncates at 1,536 chars).
- sub-agents: Task tool renamed to Agent in v2.1.63 (`Task(...)` still an alias). TodoWrite is still a built-in tool; TaskCreate/TaskGet/TaskList/TaskUpdate are separate.
- settings: no relevant changes; `model` accepts aliases or full IDs (examples use `claude-opus-5-5`).
- skill best practices: "Claude is already very smart", only add context it lacks; references one level deep; stronger wording ("MUST") is suggested only after observing failures in testing. REDIRECT: docs.claude.com → platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.
- changelog: latest 2.1.311. Only the newest ~100k of ~1.1M characters were read (file too large for one fetch); relevant: 2.1.309 oversize nested CLAUDE.md now loads only its start. No TodoWrite/AGENTS.md entries in the portion read.
- models overview: current models Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5. Model deprecations page: claude-3-5-sonnet-20241022 retired 2025-10-28, replacement claude-sonnet-5-5. REDIRECT: docs.claude.com → platform.claude.com/docs/en/about-claude/models/overview.
- Secondary sources not checked (no primary source pointed to them).

## 2026-10-27 (self-audit)
- All 8 primary URLs live, no redirects. Changelog top still 2.1.311.
- memory: project instructions also at `./.claude/CLAUDE.md`; `.claude/rules/**/*.md` (recursive, symlinks allowed, path-scoped via `paths`); imports up to 4 hops.
- skills: nested `<subdir>/.claude/skills/` and `--add-dir` folders load skills; frontmatter `allowed-tools`, `hooks`, `` !`cmd` `` shell injection; `disableSkillShellExecution` setting. `.claude/commands/` still works (older format).
- sub-agents: `.claude/agents/` scanned recursively; `permissionMode` values include `dontAsk`; frontmatter `hooks`, `mcpServers`.
- settings: `permissions.blockReadsOutsideWorkingDirectories` (v2.1.257+, `true` honored from any scope); `bypassPermissions`/`auto` defaultMode ignored from project/local settings since v2.1.257.
- models overview: same four current models. Deprecations: claude-sonnet-4-5-20250929 retires 2026-11-30 (replacement claude-sonnet-5-5).
- REDIRECT (secondary): docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview → platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (302).
