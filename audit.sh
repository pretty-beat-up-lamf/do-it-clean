#!/usr/bin/env bash
# Starts Claude Code under the do-it-clean lockdown. This is the only place the
# lockdown flags are written; README and test/run-test.sh both use it.
#   ./audit.sh <path-to-repo>       audit a repo
#   ./audit.sh self                 audit do-it-clean itself
# Anything after the target is passed on to claude (the test adds -p, --model, ...).
set -euo pipefail
TARGET=${1:?usage: ./audit.sh <path-to-repo> | self}
shift
if [ "$TARGET" != self ]; then
  # Full real path, worked out before the cd below so a relative path still means
  # what you typed. On Windows (Git Bash), cygpath turns /c/... into C:/..., so the
  # --add-dir folder and the path given to /do-it-clean are the same string.
  TARGET=$(cd "$TARGET" && pwd -P)
  if command -v cygpath >/dev/null 2>&1; then TARGET=$(cygpath -m "$TARGET"); fi
fi
cd "$(dirname "$0")"

ADD=()
[ "$TARGET" = self ] || ADD=(--add-dir "$TARGET")

# CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 in your shell would load the target's
# CLAUDE.md files as instructions, not data. A settings file can't turn it off, so it's set here.
# MSYS2_ARG_CONV_EXCL stops Git Bash on Windows from rewriting "/do-it-clean ..." into a
# Windows path, which left the session idle (issue #2). Other systems ignore it.
exec env MSYS2_ARG_CONV_EXCL=/do-it-clean CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=0 claude \
  --settings .claude/audit-settings.json --strict-mcp-config \
  --disallowedTools "mcp__*" \
  --tools "Read,Glob,Grep,Edit,Write,WebFetch,Skill" \
  ${ADD[@]+"${ADD[@]}"} "$@" "/do-it-clean $TARGET"
