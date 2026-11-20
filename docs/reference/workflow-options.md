# Workflow inputs, triggers and permissions

This page lists, for each workflow in this repository, when it runs, which permissions it asks for, which inputs and environment variables it uses, and which `aisignoff` commands it calls. For what the workflows are for, see the [workflows page](../deploy-extend/workflows.md).

!!! note
    The workflow files `signoff-request.yml` and `signoff-assistant.yml` are named in the README but their contents are not part of the material this page is based on. They are therefore not listed here, except that the README says `aisignoff-version:` can be pinned in `signoff-request.yml`.

## Triggers and permissions

| Workflow file | Name | Triggers | Permissions |
|---|---|---|---|
| `.github/workflows/file-signoff.yml` | File-signoff | `push` to `main`; `pull_request`; `merge_group`; `workflow_dispatch` | `contents: write` |
| `.github/workflows/pr-signoff.yml` | PR-signoff | `pull_request_target` on `main`, types `opened`, `edited`, `synchronize`, `reopened`, `ready_for_review` | `contents: read`, `pull-requests: write`, `issues: write` |
| `.github/workflows/signoff-badges.yml` | Signoff-Badges | `push` to `main`; `workflow_dispatch` | `contents: write` |
| `.github/workflows/signoff-release.yml` | aisignoff release report | `release` of type `published` | `contents: write` |
| `extras/workflows/file-signoff.yml` | File-signoff (example) | `push` to `main`; `pull_request`; `workflow_dispatch` | `contents: write` |
| `extras/workflows/signoff-pr-diff.yml` | aisignoff PR diff | `pull_request`, types `opened`, `edited`, `synchronize`, `reopened` | `contents: read` |
| `extras/workflows/signoff-pr-files.yml` | aisignoff PR files | `pull_request` | `contents: read` |

The workflows in `extras/workflows/` are optional examples. Copy them to `.github/workflows/` to use them (see [optional workflows](../deploy-extend/optional-workflows.md)).

## Shared organisation workflows

Three of the workflows only call a reusable workflow of the organisation, all at `@main`:

| Workflow | Calls |
|---|---|
| File-signoff | `industrial-mathematics-group/.github/.github/workflows/file-signoff.yml@main` |
| PR-signoff | `industrial-mathematics-group/.github/.github/workflows/pr-signoff.yml@main` |
| Signoff-Badges | `industrial-mathematics-group/.github/.github/workflows/signoff-badges.yml@main` |

`signoff-release.yml` and the two `extras` workflows `signoff-pr-diff.yml` and `signoff-pr-files.yml` do not call a shared workflow. They run their own steps on `ubuntu-latest` with Python 3.12 and install `aisignoff` with `pip`.

## Inputs

Inputs are passed with `with:` to the shared workflow.

| Input | Used in | Value here | Meaning |
|---|---|---|---|
| `weight` | `file-signoff.yml` | `lines` | Weights the badges by lines instead of files. |
| `aisignoff-version` | `file-signoff.yml` (commented out) | `"1.0.0rc3"` in the comment | Use another release of aisignoff than the organisation's default. |
| `aisignoff-ref` | `extras/workflows/file-signoff.yml` (commented out) | `v0.14.0` in the comment | Pin a release of aisignoff by tag; the comment gives the default as `main`. |

In `.github/workflows/file-signoff.yml` only `weight: lines` is active. In `extras/workflows/file-signoff.yml` both `weight` and `aisignoff-ref` are commented out.

## Environment variables

| Variable | Workflow | Value | Purpose |
|---|---|---|---|
| `AISIGNOFF_VERSION` | `signoff-release.yml` | `"1.0.0rc9"` | Version installed with `pip install "aisignoff==${AISIGNOFF_VERSION}"`. |
| `AISIGNOFF_VERSION` | `signoff-pr-diff.yml`, `signoff-pr-files.yml` | `"0.14.0"` | Same, for the example workflows. |
| `DESCRIPTION` | `signoff-pr-diff.yml` | `${{ github.event.pull_request.body }}` | The pull request description, written to a file and passed to `--declare-from`. |
| `AUTHOR` | `signoff-pr-diff.yml` | `${{ github.event.pull_request.user.login }}` | The pull request author, passed to `--author`. |
| `BASE` | `signoff-pr-files.yml` | `${{ github.event.pull_request.base.sha }}` | Base commit for the list of changed files. |
| `HEAD` | `signoff-pr-files.yml` | `${{ github.event.pull_request.head.sha }}` | Head commit for the list of changed files. |
| `GH_TOKEN` | `signoff-release.yml` | `${{ github.token }}` | Authenticates `gh release upload`. |
| `TAG` | `signoff-release.yml` | `${{ github.event.release.tag_name }}` | The release the reports are uploaded to. |

In `signoff-pr-diff.yml`, `BASE` is also a shell variable inside the step, set with `git rev-parse HEAD^1`. It is not the same as the `BASE` environment variable of `signoff-pr-files.yml`.

## aisignoff commands used

| Workflow | Command | Purpose |
|---|---|---|
| `signoff-release.yml` | `aisignoff report --landed` | Text summary per axis. |
| `signoff-release.yml` | `aisignoff report --tree --landed` | Level mix per folder. Both text outputs go into `aisignoff-report.txt`. |
| `signoff-release.yml` | `aisignoff report --json --landed` | Every file with its levels, names and source, as `aisignoff-report.json`. |
| `signoff-release.yml` | `aisignoff report --html <path> --landed` | Interactive folder report, as `aisignoff-report.html`. |
| `signoff-release.yml` | `aisignoff lint --landed` | If it fails, a warning is emitted and the reports list undeclared files; the step does not fail. |
| `signoff-pr-diff.yml` | `aisignoff diff "$BASE" --markdown --depth 2 --declare-from <description file> --author "$AUTHOR"` | Levels of the added and removed lines, written to the job summary. |
| `signoff-pr-files.yml` | `aisignoff report --json` | Levels per file, used to build the table and annotations for the changed files. |

`--landed` makes the release reports describe the code at the release tag even when the release is cut from a branch whose commits would not count as landed otherwise. The workflow comments name aisignoff 0.12 as the first version with `--landed` and `--declare-from`.

The workflows that call shared organisation workflows (File-signoff, PR-signoff, Signoff-Badges) run their `aisignoff` commands inside those workflows, so the commands are not visible in this repository.

## Checkout settings

| Workflow | `fetch-depth` | Reason given in the file |
|---|---|---|
| `signoff-release.yml` | `0` | The whole history, for line-by-line declarations (`[history]`). |
| `signoff-pr-diff.yml` | `0` | The base commit and the history behind each line. |
| `signoff-pr-files.yml` | `0` | The base commit is needed for the diff. |
