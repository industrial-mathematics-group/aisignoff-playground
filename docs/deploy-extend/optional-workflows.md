# Optional workflows in extras/

The folder `extras/workflows/` holds three workflows that this repository does not run. Copy the ones you want into `.github/workflows/` of your own repository. The PR diff and PR files workflows only read the repository and report; the file-signoff example is a plain check.

| File | What it does |
|---|---|
| `file-signoff.yml` | An example of the File-signoff check |
| `signoff-pr-diff.yml` | Writes the levels of the lines a pull request changes to the job summary |
| `signoff-pr-files.yml` | Writes a table of the changed files and their levels, and annotates them in the pull request |

!!! note
    The files in `extras/` do not run here. A workflow only runs from `.github/workflows/`.

## file-signoff.yml

This is an example of the check that [the repository's own workflow](workflows.md) already runs. It calls the organisation's shared workflow `industrial-mathematics-group/.github/.github/workflows/file-signoff.yml@main`, which checks with aisignoff that every file is declared in `SIGNOFF.toml` or by inline tags. On pushes to the default branch it also publishes the file badges.

Triggers: `push` to `main`, `pull_request` and `workflow_dispatch`. The permission is `contents: write`.

The `with:` block is commented out. Two inputs are shown there:

| Input | Meaning |
|---|---|
| `weight: lines` | Weight the badges by lines instead of files |
| `aisignoff-ref: v0.14.0` | Pin a release of aisignoff by tag; the default is `main` |

The workflow in `.github/workflows/file-signoff.yml` is the current form: it also triggers on `merge_group` and uses `aisignoff-version` instead of `aisignoff-ref`. See [Updating and pinning aisignoff](updating-aisignoff.md).

## signoff-pr-diff.yml

This shows reviewers the declarations of just the lines a pull request changes. It is most useful with `[history]` enabled in `SIGNOFF.toml`, so that lines take declarations from git. Without it, the changed lines take the file-level declarations. See [line-level declarations](../concepts/line-level-history.md).

It runs on pull requests when they are `opened`, `edited`, `synchronize`d or `reopened`, with `contents: read`. The steps are:

1. Check out the repository with `fetch-depth: 0`, so the base commit and the history behind each line are available.
2. Install aisignoff at the version in `AISIGNOFF_VERSION` (set to `1.0.0rc9` in the example).
3. Take `BASE=$(git rev-parse HEAD^1)`, the first parent of the merge preview, which is the base branch as this run merged it.
4. Write the pull request description to a file and run:

```bash
aisignoff diff "$BASE" --markdown --depth 2 --declare-from "$RUNNER_TEMP/description.md" \
  --author "$AUTHOR"
```

The output goes to the job summary under the heading "AI signoff of the changed lines".

What it shows, per the comments in the file:

- the levels of the added and removed lines per folder
- attestations the pull request adds
- how the repository's shares move

`--declare-from` declares the pull request's lines from its description, read the way aisignoff reads the merge or squash commit when the repository's default commit message is "Pull request title and description". The description can contain "Key: value" lines (`AI-Generation`, `Human-Review`, `AI-Review` and the names) or the ticked checkboxes of the pull request template. A pull request into a branch other than the default one declares nothing; the pull request that lands those lines on the default branch declares them.

If `aisignoff diff` fails, the step writes "aisignoff diff failed, see the log" to the summary instead of failing the job.

## signoff-pr-files.yml

This shows reviewers the declarations of the files a pull request changes. It does three things:

- writes a table of the changed files and their levels to the job summary
- annotates each changed file in the "Files changed" tab with its levels, and marks files without a valid declaration as errors
- reminds the author to update `SIGNOFF.toml` when the pull request does not touch it

It runs on `pull_request` with `contents: read`. The steps are:

1. Check out with `fetch-depth: 0`, because the base commit is needed for the diff.
2. Install aisignoff at `AISIGNOFF_VERSION` (`1.0.0rc9` in the example).
3. List the changed files with `git diff --name-only --diff-filter=d -z "$BASE...$HEAD"`, using the pull request's base and head SHAs. Deleted files are left out.
4. Run `aisignoff report --json` and join the changed files with the report using an inline Python script.

The summary table has the columns File, Levels, Declared in and Valid. Files that are ignored by `.gitignore` or excluded in `SIGNOFF.toml` are not in the report and are skipped. If `SIGNOFF.toml` (or `AIDECL.toml`) is not among the changed files, the workflow adds a note suggesting `aisignoff annotate` to update the declarations when the pull request changes how files were created or reviewed.

## What they read and what they do not do

| | `signoff-pr-diff.yml` | `signoff-pr-files.yml` |
|---|---|---|
| Reads | Git history, `SIGNOFF.toml`, the pull request description | Git diff, `SIGNOFF.toml` and inline tags through `aisignoff report --json` |
| Writes to | Job summary | Job summary and annotations in *Files changed* |
| Permission | `contents: read` | `contents: read` |

Both only read the repository, so they also work for pull requests from forks. Neither fails the check on its own. In `signoff-pr-files.yml`, files without a valid declaration appear as error annotations, but the job does not fail because of them. Failing a pull request is the job of `aisignoff lint`, which the [File-signoff workflow](workflows.md) runs.

## Using them

1. Copy the file from `extras/workflows/` to `.github/workflows/`.
2. Set `AISIGNOFF_VERSION` to the release you use. Keep it the same as in your other workflows and your local install; see [Updating and pinning aisignoff](updating-aisignoff.md).
3. Open a pull request and read the job summary of the new workflow.
