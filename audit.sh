#!/usr/bin/env bash
# Starts Claude Code under the do-it-clean lockdown. This is the only place the
# lockdown flags are written; README and test/run-test.sh both use it.
#   ./audit.sh <path-to-repo>       audit a repo
#   ./audit.sh self                 audit do-it-clean itself
# Anything after the target is passed on to claude (the test adds -p, --model, ...).
set -euo pipefail
cd "$(dirname "$0")"
TARGET=${1:?usage: ./audit.sh <path-to-repo> | self}
shift

ADD=()
[ "$TARGET" = self ] || ADD=(--add-dir "$TARGET")

# CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 in your shell would load the target's
# CLAUDE.md files as instructions, not data. A settings file can't turn it off, so it's set here.
exec env CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=0 claude \
  --settings .claude/audit-settings.json --strict-mcp-config \
  --tools "Read,Glob,Grep,Edit,Write,WebFetch,Skill" \
  ${ADD[@]+"${ADD[@]}"} "$@" "/do-it-clean $TARGET"
