# Setting up the repository on GitHub

Before the checks and badges work, a new repository needs a few settings on GitHub. Five steps cover it, and the commit message setting in step 2 is the one that matters most.

## 1. Create the repository and push

Create an empty repository on GitHub, then push your local `main` to it:

```bash
git remote add origin <url> && git push -u origin main
```

## 2. Allow merge commits with the pull request description

Open *Settings → General → Pull Requests* and do the following:

- Allow merge commits. Also allow squash merging if you want to try [scenario 5](../usage/scenarios.md).
- Set the default commit message of both merge methods to **Pull request title and description**.

!!! warning
    Without this setting the declaration never reaches git.

Here is why. With line-level declarations (`[history]` in `SIGNOFF.toml`), aisignoff reads each line's declaration from the commit that landed it on `main`. For a pull request, that is the merge or squash commit. The declaration you tick in the pull request template is part of the description. The commit message contains that description only if the default message is **Pull request title and description**. With any other default, the ticked boxes are not written into the commit, and the lines fall back to the annotations in `SIGNOFF.toml`.

## 3. Require the checks on `main`

Open *Settings → Rules → Rulesets* (or *Branches*) and add a rule for `main` that:

- requires a pull request, and
- requires the checks **File-signoff** and **PR-signoff**.

If you want to try the plain-push scenario after this rule is in place, leave direct pushes allowed for yourself.

## 4. Check the first run

Open the *Actions* tab. The first **File-signoff** run should be green, and its job summary should show the folder tree of declarations.

## 5. The badges branch

The first push to `main` after the setup creates the `badges` branch. The file badges in the README are published there on pushes to `main`.

- The pull request badges (second row) show "no declarations yet" until a declared pull request is merged.
- Don't protect `badges` against pushes by `github-actions[bot]`, or the workflows can't update the badges.

## Next steps

Continue with [your first pull request](first-pull-request.md), or see what each workflow does on the [workflows](../deploy-extend/workflows.md) page.
