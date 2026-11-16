# Line-level declarations and merge methods

With `[history]` turned on, aisignoff declares every line of a file separately instead of giving the whole file one declaration. Each line takes the declaration of the commit that landed it on `main`.

## What `[history]` does

This repository enables it in `SIGNOFF.toml`:

```toml
[history]
enabled = true
merge-method = "merge"
```

For each line, aisignoff looks at the commit that brought the line onto `main` and reads the declaration in that commit's message. The declaration is either the ticked pull request template or "Key: value" lines such as `AI-Generation: G2`. If that commit declares nothing, the line falls back to the file-level declaration from the [annotations](where-declarations-live.md). In this repository the fallback is G0 · H2 · A0.

A file can therefore contain lines at different levels. `aisignoff report --files` shows the share of each declaration for files with mixed lines, and `aisignoff diff HEAD^1 --files` shows the levels of the lines a commit added.

The `[history]` table also has a commented-out option, `undeclared = "error"`. Uncommenting it requires a declaration from every commit that lands on `main`.

## Why the pull request template becomes the declaration

A pull request description is not stored in git. The declaration only reaches the history if it is part of the commit message of the merge or squash commit. That is why the repository setup sets the default commit message of merge and squash merges to **Pull request title and description** (see [setting up the repository on GitHub](../getting-started/setup-on-github.md)). With that setting, the ticked boxes of the template are copied into the message of the commit that lands on `main`, and aisignoff reads them from there.

Without this setting the declaration never reaches git, and the lines fall back to the file-level declaration.

## Merge methods

`merge-method` tells aisignoff how pull requests land on `main`. It decides which commit's message declares the lines.

| `merge-method` | What lands on `main` | Which declaration counts |
|---|---|---|
| `"merge"` (default) | A merge commit, plus the branch's own commits | The merge commit's description declares the lines. A branch commit with its own declaration, for example `AI-Generation: G3`, raises the generation of the lines it wrote. |
| `"squash"` | One squash commit | The squash commit's description declares all its lines. The generation declared in the branch commits is ignored. |
| `"rebase"` | The branch's commits, replayed | Accepted as a value in `SIGNOFF.toml`; this repository does not use it. |

The value in `SIGNOFF.toml` must match how you actually merge. This repository uses `"merge"`.

On `main`, the reviewer of lines declared through a merge commit is the merge commit's author, that is, whoever clicked *Merge*.

## Example: a merged pull request

Open a pull request that changes `src/playground/stats.py` and tick G2, Claude Opus, H1 and A1. After a merge commit:

- `aisignoff report --files` shows `stats.py` as mostly G0 · H2 · A0, with a share at the ticked levels.
- `aisignoff diff HEAD^1 --files` shows the added lines at G2 · H1 · A1.

## Stacked pull requests

Only a pull request into `main` is checked by PR-signoff, and only its description declares lines. Take branch `a` from `main`, branch `b` from `a`, with PR A (`a` → `main`) and PR B (`b` → `a`):

- PR B's description is not checked by aisignoff, because it does not go into the default branch.
- If you merge B into A and then A into `main`, A's description declares all the lines, B's included.
- If you merge A first and GitHub retargets B to `main`, B's description now counts for the lines B's merge brings in.

## Switching to squash merges

To try the squash method, set `merge-method = "squash"` in `SIGNOFF.toml` and land that change first. Then squash-merge a pull request with several commits, some with `AI-Generation: G3` in their messages. The squash commit's description declares all its lines, and the branch commits' generation is ignored.

For the exact checks, see [try-out scenarios](../usage/scenarios.md).

## Frozen lines

Declarations worked out from history can be frozen into a snapshot so that later changes to annotations do not alter them. See [snapshots and freezing](snapshots-and-freeze.md).
