# Standards

Durable principles. These describe *what good looks like* independent of any model or tool version. Edit by hand only; the self-audit may suggest changes but must not rewrite this file wholesale.

1. **Minimal.** Every line must earn its place. If a capable model would do the right thing without it, it's a prune candidate.
2. **Specific to this repo.** Keep instructions the model couldn't infer from the code: commands, conventions, gotchas, non-obvious constraints. Drop generic advice ("write clean code").
3. **One source of truth, short and scannable.** Each rule lives in exactly one file; other files link to it instead of restating it. Keep links one level deep (A → B, not A → B → C). Rules that must always apply are written out where they apply, not hidden behind a link. Length limits come from current guidance, not from this file.
4. **No contradictions.** Two files must never give conflicting directions for the same situation.
5. **True today.** Paths, commands, tools, flags, and model names that are referenced must actually exist.
6. **Calm wording.** Prefer plain statements over shouting (ALL CAPS, "MUST", "NEVER EVER"), unless current guidance in `sources.md` says otherwise.
7. **Human in the loop.** Automation proposes changes; a person approves them.
8. **Safe.** Instruction and config files contain no secrets. They don't turn off human review. They don't send data off the machine without the user knowing. They don't contain text that tries to steer other AI agents.
9. **Durable wording.** Names that change over time (models, versions, prices) appear only in dated records, such as test results, the digest, and `models.md`. Everywhere else, use an alias or a general description ("your default model"). Anything that has to be named exactly, like a setting or a file location, needs a check that catches it when it goes stale.
