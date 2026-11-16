# Usage overview

This section covers the everyday tasks in aisignoff-playground: telling the repository how a change was made and checked, declaring files that are already in `main`, and reading what the checks produce.

## Everyday tasks

| Task | When you need it | Page |
|---|---|---|
| Declare a pull request | Every pull request into `main`. You tick the generation, model, human review and AI review boxes in the description. | [Declaring a pull request](declaring-a-pull-request.md) |
| Declare existing files | Files already in `main` that need a declaration, or a review you did afterwards. A form or the @signoff assistant opens a pull request that changes `SIGNOFF.toml`. | [Declaring existing files with @signoff](signoff-requests.md) |
| Write declarations in commit messages | You commit directly or want to declare lines with "Key: value" lines. | [Inline tags and commit message trailers](inline-tags-and-commit-trailers.md) |
| Try the behaviour | You want to see what the checks do for a plain push, a pull request, stacked pull requests, a squash merge, a freeze or a merge queue. | [Try-out scenarios](scenarios.md) |
| Read release reports | You want to see how a published release was made and reviewed, or archive it with a DOI. | [Release reports and Zenodo](release-reports.md) |

## Reading the results

Each pull request into `main` gets labels (`ai:G*`, `human:H*`, `ai-review:A*`) from the PR-signoff check. On `main`, the File-signoff run writes a folder tree to its job summary and uploads the folder report as the `aisignoff-report` artifact. It also updates the file badges. The badges for merged pull requests come from the Signoff-Badges workflow.

For what these outputs are and how they are produced, see the [concepts](../concepts/index.md) section. To run the same reports on your own machine, see [Running aisignoff locally](../getting-started/local-commands.md).

## Where to start

- New to the repository: follow [Your first pull request](../getting-started/first-pull-request.md), then [Declaring a pull request](declaring-a-pull-request.md).
- A check is red and you don't know why: see [Troubleshooting](../troubleshooting.md).
- The meaning of G, H and A levels: see [Generation, human review and AI review levels](../concepts/declaration-levels.md).
