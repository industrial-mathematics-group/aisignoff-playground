# The GitHub workflows

The repository has six workflows in `.github/workflows/`. Four of them call shared workflows from the organisation's `industrial-mathematics-group/.github` repository, one is a standalone workflow, and two (the signoff request and the assistant) are described in the README but their files are not part of the material shown here.

| Workflow file | What it does | Runs on |
|---|---|---|
| `file-signoff.yml` | Checks that every file (with `[history]`, every line) is declared; publishes the file badges | `push` to `main`, `pull_request`, `merge_group`, `workflow_dispatch` |
| `pr-signoff.yml` | Checks the AI declaration ticked in each pull request template | `pull_request_target` into `main` |
| `signoff-badges.yml` | Summarises the declarations of merged pull requests as badges | `push` to `main`, `workflow_dispatch` |
| `signoff-release.yml` | Attaches the AI signoff reports to each published release | `release` (`published`) |
| `signoff-request.yml`, `signoff-assistant.yml` | Issue form and @signoff assistant that open pull requests changing `SIGNOFF.toml` | see below |

## File-signoff

`file-signoff.yml` calls `industrial-mathematics-group/.github/.github/workflows/file-signoff.yml@main`. It runs `aisignoff` to check that every file is declared. With `[history]` enabled in `SIGNOFF.toml`, every line must be declared. The policy in `SIGNOFF.toml` is checked as well. On pushes to the default branch it also publishes the file badges.

Triggers:

- `push` to `main`
- `pull_request`
- `merge_group`, so that with a merge queue the commit that will land is checked
- `workflow_dispatch`, to start it by hand

Input: `weight: lines` weights the badges by lines instead of files. The file also contains a commented-out `aisignoff-version` input to use another release of aisignoff than the organisation's default (see [updating aisignoff](updating-aisignoff.md)).

Permissions: `contents: write`.

Its output is described in the README: the folder tree in the job summary, the folder report as the artifact `aisignoff-report`, and on `main` the file badges on the `badges` branch.

## PR-signoff

`pr-signoff.yml` calls the organisation's `pr-signoff.yml@main`. It checks the AI declaration ticked in the pull request template.

- Trigger: `pull_request_target` for pull requests into `main`, with the types `opened`, `edited`, `synchronize`, `reopened` and `ready_for_review`.
- Because `edited` is included, the check reruns when you tick boxes in the description. No new push is needed.
- Permissions: `contents: read`, `pull-requests: write`, `issues: write`.

According to the README, it validates the ticked template and sets the labels `ai:G*`, `human:H*` and `ai-review:A*`. Pull requests that target another branch than `main` are not checked by it.

## Signoff-Badges

`signoff-badges.yml` calls the organisation's `signoff-badges.yml@main`. It summarises the AI declarations of the pull requests merged into the default branch as README badges (the second badge row).

- Triggers: `push` to `main` and `workflow_dispatch`.
- Permissions: `contents: write`.

## Signoff release report

`signoff-release.yml` does not call a shared workflow. It is a copy of aisignoff's `examples/workflows/signoff-release.yml`. It runs when a release is published and adds three files to that release, describing the code at the release tag:

- `aisignoff-report.txt`: the summary per axis and the level mix per folder
- `aisignoff-report.json`: every file with its levels, names and source
- `aisignoff-report.html`: the interactive folder report

Details:

- Trigger: `release` with type `published`.
- Permissions: `contents: write`, to upload the release assets.
- It checks out the tag with `fetch-depth: 0`, so the line-by-line declarations from `[history]` are available. It installs aisignoff with `pip`, pinned by `AISIGNOFF_VERSION` (`1.0.0rc9`).
- All reports use `--landed`, so a release cut from a release branch is reported as it is.
- The reports are written to `$RUNNER_TEMP`, outside the work tree. Otherwise lint would count them as undeclared files.
- It also runs `aisignoff lint --landed`. If files have no valid declaration, this only raises a warning annotation. It does not fail the workflow, and the reports list those files as undeclared.
- The upload uses `gh release upload --clobber` with `GH_TOKEN` and the tag name from the release event.

See [release reports](../usage/release-reports.md) for how to use the assets.

## Signoff request and assistant

According to the README, `signoff-request.yml` and `signoff-assistant.yml` provide the issue form *Signoff: declare or attest files* and the @signoff assistant. Both open pull requests that change `SIGNOFF.toml`. The workflow files themselves are not covered here, so triggers and permissions are not listed. For how to use them, see [declaring existing files with @signoff](../usage/signoff-requests.md).

## Permissions at a glance

| Workflow | `contents` | `pull-requests` | `issues` |
|---|---|---|---|
| `file-signoff.yml` | write | – | – |
| `pr-signoff.yml` | read | write | write |
| `signoff-badges.yml` | write | – | – |
| `signoff-release.yml` | write | – | – |

## Shared organisation workflows

| Local workflow | Calls |
|---|---|
| `file-signoff.yml` | `industrial-mathematics-group/.github/.github/workflows/file-signoff.yml@main` |
| `pr-signoff.yml` | `industrial-mathematics-group/.github/.github/workflows/pr-signoff.yml@main` |
| `signoff-badges.yml` | `industrial-mathematics-group/.github/.github/workflows/signoff-badges.yml@main` |

The shared workflows are referenced at `@main`, so changes in the organisation repository apply here without a change in this repository.

!!! note
    The two required checks in the `main` ruleset are **File-signoff** and **PR-signoff**. See [setting up the repository on GitHub](../getting-started/setup-on-github.md).
