# Coordinated publishing milestone workflow

User instruction recorded 25 September 2026: on significant milestones, review `git diff`, generate a detailed untracked commit-message file based on the diff, then commit and push both repositories.

Research repository: `https://github.com/TheAlchemistNerd/sokointel-financial-research.git`.
Platform repository: `https://github.com/TheAlchemistNerd/sokointel-platform.git`.

## Before committing

1. Inspect status, unstaged/staged diffs and untracked files in each repository. Account for changes from other active work; do not discard them or overwrite source material.
2. Review the actual final scope, generated asset inventory and validation results. Confirm source traces, links and metadata match the output. Keep credentials, private deployment files, databases, temporary Office files and build caches out of the commit.
3. Write one detailed message per repository in an untracked/ignored temporary location outside the delivered assets. Derive the title and body from the actual reviewed diff, not the original plan. Include the problem, resulting behaviour/assets, meaningful validation and remaining limitations. Use `git commit --file <path>` to preserve paragraphs exactly.
4. Stage the intended paths, inspect the staged diff/stat and commit. Record the resulting commit hash and the message-file location in the milestone handoff.
5. Check the configured remote and branch, then push normally. Never force-push or rewrite unrelated history as part of this workflow. A review or network failure is not a successful push; retain the local commit and report what remains.
6. Verify the remote head after pushing. Record research and platform outcomes separately. A Git push does not establish that Railway deployed successfully, imported new catalog content or regenerated all runtime editions.

## Publication verification

The platform release needs deployed code, the catalog import with the intended update behaviour, and accessible edition files. If the background worker generates files independently, it and the web service must access the same persistent private storage. Confirm the four project pages, article content, workbook downloads and a member download after deployment.

Keep status precise: source complete, generated, visually reviewed, committed, pushed, deployed, imported and published are different milestones. Preserve the original research and evidence even when a new branded edition becomes the preferred download.
