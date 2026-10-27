# Sources

Where each run looks for **current** guidance. URLs only: no copied content, so nothing here goes stale except the links themselves.

If a link is dead or redirects, the run reports it and the self-audit proposes a replacement.

**Security:** every domain listed here must also be in the WebFetch allowlist in `.claude/audit-settings.json`, and nothing else should be. Anything not on the allowlist is blocked.

## Primary (always check)
- Claude Code docs, memory / CLAUDE.md: https://code.claude.com/docs/en/memory
- Claude Code docs, skills: https://code.claude.com/docs/en/skills
- Claude Code docs, subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code docs, settings: https://code.claude.com/docs/en/settings
- Claude Code docs, permissions (rule syntax, modes): https://code.claude.com/docs/en/permissions
- Claude Code docs, CLI reference (flags used in README.md and test/run-test.sh): https://code.claude.com/docs/en/cli-reference
- Skill authoring best practices (file length, structure, references): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Claude Code changelog: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md (too big to read whole: read only entries newer than `Last checked` in the digest; on a first run, the newest ~20 versions)
- Anthropic models overview: https://platform.claude.com/docs/en/about-claude/models/overview
- Model deprecations: https://platform.claude.com/docs/en/about-claude/model-deprecations

## Secondary (check if the primary sources point to them or a new model shipped)
- Anthropic engineering blog: https://www.anthropic.com/engineering
- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- AGENTS.md convention: https://agents.md

## Rules
- Prefer primary sources over secondary ones, and secondary ones over everything else.
- Social posts and talks are leads, not evidence: confirm them in a primary source before citing them.
