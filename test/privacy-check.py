#!/usr/bin/env -S python3 -I
"""do-it-clean privacy check: plain code, no AI.

Stops a push if it would publish anything about the repos you've audited or
about you. It checks every line the outgoing commits add, their messages, and
their author and committer details.

What counts as private (all from gitignored files, so this script names nothing):
  - each audited repo's name, from the file name and title of every report in
    reports/private/
  - each repo and owner listed in targets.md
  - each line of private-words.txt (your name, email, username, anything else)
  - absolute home-folder paths on a Mac or Linux machine

A repo name that's already in the published copy of the repo is a common word
(like "skills"), so it's skipped and listed instead of blocking every push.
Lines from private-words.txt are never skipped.

Usage:
  privacy-check.py              check commits that aren't on any remote yet
  privacy-check.py <A>..<B>     check a specific range
  As the pre-push hook, git passes the refs being pushed on stdin.
"""
import glob, os, re, subprocess, sys

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
os.chdir(ROOT)
ZERO = "0" * 40
PATHS = [r"/(?:Users|home)/[^/\s]+"]


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True).stdout


def report_names():
    """Repo names from report titles and targets.md."""
    names = set()
    for f in glob.glob("reports/private/*.md"):
        m = re.match(r"do-it-clean-(.+)-\d{4}-\d{2}-\d{2}\.md$", os.path.basename(f))
        if m:
            names.add(m.group(1))
        with open(f, errors="ignore") as fh:
            m = re.match(r"# do-it-clean report: (.+), \d{4}-\d{2}-\d{2}", fh.readline())
        if m:
            title = m.group(1)
            names.add(re.sub(r"\s*\(.*\)", "", title).strip())
            names.update(w for p in re.findall(r"\(([^)]*)\)", title) for w in p.split() if "-" in w)
    if os.path.exists("targets.md"):
        for line in open("targets.md"):
            m = re.match(r"\s*-\s*(\S+)", line)
            if m:
                names.update(m.group(1).split("/"))
    return {n for n in names if len(n) >= 3}


def private_words():
    if not os.path.exists("private-words.txt"):
        return set()
    return {l.strip() for l in open("private-words.txt") if l.strip() and not l.startswith("#")}


def word_re(w):
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(w) + r"(?![A-Za-z0-9])", re.I)


def ranges_from_stdin():
    """Pre-push hook input: <local ref> <local sha> <remote ref> <remote sha> per line."""
    out = []
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 4 or parts[1] == ZERO:
            continue  # deleting a branch publishes nothing
        local, remote = parts[1], parts[3]
        out.append(f"{remote}..{local}" if remote != ZERO else f"{local} --not --remotes")
    return out


def main():
    if os.path.basename(sys.argv[0]) == "pre-push":  # run by git, which passes the refs on stdin
        ranges = ranges_from_stdin() or ["HEAD --not --remotes"]
    else:
        ranges = sys.argv[1:] or ["HEAD --not --remotes"]

    # A new branch has no upstream yet, so compare against the published main instead.
    published = (git("rev-parse", "--verify", "-q", "@{upstream}").strip()
                 or git("rev-parse", "--verify", "-q", "origin/main").strip() or None)
    skipped, checks = [], []
    for n in sorted(report_names()):
        if published and subprocess.run(["git", "grep", "-I", "-q", "-i", "-w", "-F", n, published]).returncode == 0:
            skipped.append(n)
        else:
            checks.append((n, word_re(n)))
    checks += [(w, word_re(w)) for w in sorted(private_words())]
    checks += [("home-folder path", re.compile(p)) for p in PATHS]

    hits = []
    for r in ranges:
        for sha in git("rev-list", *r.split()).split():
            meta = git("show", "-s", "--format=%an <%ae>%n%cn <%ce>%n%B", sha)
            diff = git("show", "--format=", "--no-color", "--unified=0", sha)
            added = [l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++")]
            files = [l[6:] for l in diff.splitlines() if l.startswith("+++ b/")]
            for where, lines in (("message or author", meta.splitlines()), ("file names", files), ("added lines", added)):
                for line in lines:
                    for label, rx in checks:
                        if rx.search(line):
                            hits.append(f"  {sha[:7]} {where}: matches {label!r}: {line.strip()[:100]}")

    if skipped:
        print("privacy-check: skipped (already in the published repo, so treated as common words): " + ", ".join(skipped))
    if hits:
        print("privacy-check: BLOCKED. These would publish private details:")
        print("\n".join(dict.fromkeys(hits)))
        print("Fix the commits, then push again.")
        return 1
    print(f"privacy-check: OK ({len(checks)} private terms checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
