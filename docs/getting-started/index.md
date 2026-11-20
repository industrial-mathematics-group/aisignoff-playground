# Getting started overview

This section takes you from an empty GitHub repository to a first declared pull request, and shows the local commands for checking declarations on your own machine. Each page builds on the one before it.

## What you need

- **A GitHub repository.** The setup is built around GitHub: the workflows run in GitHub Actions, and the declarations of a pull request are read from its description once it is merged. Use a new repository or an existing one.
- **A browser.** Everything in the first pull request, from editing a file to merging, can be done in the GitHub web interface. You do not need a command line for it.
- **aisignoff (optional).** The checks in CI run it for you. Install it locally only if you want to run `aisignoff lint` or the report commands yourself. The README installs it with `pipx install aisignoff==1.0.0rc9`.

!!! note
    The playground reuses the organisation's shared workflows from `industrial-mathematics-group/.github`. You do not have to install the checks yourself; the files in `.github/workflows/` call them.

## Order of the pages

1. [Setting up the repository on GitHub](setup-on-github.md): push the files, set the merge commit message, require the checks and verify the first run. The commit message setting matters most, because without it a declaration never reaches git.
2. [Your first pull request](first-pull-request.md): change a file in the browser, watch the checks fail on the unfilled template, tick the AI declaration and merge.
3. [Running aisignoff locally](local-commands.md): install aisignoff at the version CI uses and run `lint`, `report --files`, `diff HEAD^1 --files` and `report --json`.

## Where to go next

After these three pages, the [concepts](../concepts/index.md) section explains the generation, human review and AI review levels, and where declarations are stored. The [usage](../usage/index.md) section covers everyday tasks.
