# Install and extend overview

This playground is set up with workflows that call the organisation's shared workflows, plus a few optional workflows you can copy. This section explains how to adopt the same setup in another repository and how to keep it current.

## Three ways to adopt the setup

### Reuse the organisation's workflows

The workflows in `.github/workflows/` of this repository are short. `file-signoff.yml`, `pr-signoff.yml` and `signoff-badges.yml` each call a workflow from `industrial-mathematics-group/.github` with `uses: industrial-mathematics-group/.github/.github/workflows/<name>.yml@main`. The checking logic lives in the organisation's repository, so your repository only carries the trigger, the permissions and any inputs.

To adopt this, copy the workflow files you need into `.github/workflows/` of your repository. [The GitHub workflows](workflows.md) describes what each one does, which triggers and permissions it uses, and what it needs.

Reusing the workflows also requires the repository settings described in [Setting up the repository on GitHub](../getting-started/setup-on-github.md). In particular, the default commit message for merge commits must be **Pull request title and description**, otherwise the ticked declaration never reaches git.

### Copy the optional workflows

The `extras/workflows/` folder holds workflows that are not active in this repository. You copy them into `.github/workflows/` if you want them:

- a file-signoff example,
- a summary of the levels of the lines a pull request changes,
- a table and annotations of the files a pull request changes.

They only read the repository and do not fail a check on their own. See [Optional workflows in extras/](optional-workflows.md).

### Pin versions

Several places set which release of aisignoff runs:

- the organisation's default, used by `file-signoff.yml` unless you override it,
- the `aisignoff-version` input of `file-signoff.yml`,
- the `AISIGNOFF_VERSION` variable in `signoff-release.yml` and in the workflows under `extras/workflows/`.

Keep your local install at the same version as CI: a snapshot written by another version than CI's can fail the check. See [Updating and pinning aisignoff](updating-aisignoff.md).

## Pages in this section

| Page | What it covers |
|---|---|
| [The GitHub workflows](workflows.md) | What each workflow in `.github/workflows/` does, with its triggers and permissions |
| [Optional workflows in extras/](optional-workflows.md) | The workflows to copy into `.github/workflows/` and what they read |
| [Updating and pinning aisignoff](updating-aisignoff.md) | Where the aisignoff version is set and why CI and local installs should match |
| [Running the workshop](workshop-material.md) | The `workshop/` folder and what a facilitator prepares |

For the exact inputs and variables of each workflow, see the [workflow reference](../reference/workflow-options.md).
