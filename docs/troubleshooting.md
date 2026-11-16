# Troubleshooting

Common problems with the signoff checks in this repository, what causes them and how to fix them. For any red check, open **Details** on it first: the message says which rule failed.

## A check is red after ticking the declaration

The pull request template must be filled in as follows. The PR-signoff check reports an error for each of these:

| Symptom | Cause | Fix |
|---|---|---|
| Error about more than one generation box | G1 and G2 (or any two G boxes) are ticked | Keep exactly one generation box, the highest level of any substantial part |
| Error about a missing model | G1, G2 or G3 is ticked but no model is | Tick the model, or write it under **Other:** |
| Policy failure | Only H0 is ticked, and this repository requires at least H1 | Tick the human review level you actually did, H1 or higher |
| Policy failure on a G3 change | G3 needs at least A1 | Have a fresh AI session review the change and tick A1 or higher, or declare the generation honestly at the level that applies |
| A2 or A3 rejected | The report is not committed or linked, or the `AI-Review-Findings:` line is empty | Name the model and the report, and fill in `AI-Review-Findings:` (`none`, `trivial`, `minor`, `major` or `critical`). For A0 and A1, leave the line empty |
| `TODO` error with an untouched template | Nothing is ticked yet | Tick the boxes in the description |

A `major` or `critical` finding has to be fixed and reviewed again before merging.

## The check does not rerun after ticking

Editing the description reruns PR-signoff on the `edited` event, without a new push. If the check still shows the old result:

1. Reload the page.
2. If it is still old, untick and tick one box again.

Checks on stacked pull requests are a separate case. PR-signoff only checks pull requests into `main`, so a pull request into another branch is not checked. See [line-level declarations](concepts/line-level-history.md).

## "Merge pull request" is greyed out

The checks are still running or red, or the ruleset for `main` requires an approval. Wait for the checks, fix any red one, and review the ruleset under *Settings → Rules*.

## The declaration is missing on main

If a merged pull request does not show its levels in `aisignoff report --files`, the ticked declaration did not reach git. The declaration travels in the merge commit message, so the default commit message must contain the pull request description.

Check *Settings → General → Pull Requests*:

- merge commits are allowed (and squash merging, if you use it),
- the default commit message of each enabled method is **Pull request title and description**.

Also check that `merge-method` in `SIGNOFF.toml` matches how you actually merge (`merge`, `squash` or `rebase`). See [Setting up the repository on GitHub](getting-started/setup-on-github.md).

## The snapshot check fails

`aisignoff lint` checks `SIGNOFF.snapshot.json` by working it out again. It fails if:

- the snapshot was edited by hand, for example a level changed,
- the snapshot was written by another aisignoff version than the one CI runs.

Run `aisignoff freeze --check` to run the snapshot check on its own. To fix a version mismatch, install the same aisignoff version locally as CI uses (see [Updating and pinning aisignoff](deploy-extend/updating-aisignoff.md)) and write the snapshot again with `aisignoff freeze`. Don't edit the snapshot by hand. See [Snapshots and freezing](concepts/snapshots-and-freeze.md).

## Lint reports undeclared files or a policy error

- **A file has no valid declaration:** the `**` annotation in `SIGNOFF.toml` covers everything by default. If a file is not covered, check that it is not excluded and that its annotation is valid.
- **Policy error:** a declared level is below the minimum in `[policy]`, for example `results/**` set to `AI-Review = "A0"` while it is G3.
- **Warning for an annotation path that matches nothing:** lint passes but warns. `aisignoff lint --strict` would fail on it.

## Merge conflicts in SIGNOFF.toml from bot pull requests

When several signoff requests run at once, each bot pull request adds an entry at the end of `SIGNOFF.toml`. The second one then shows "This branch has conflicts".

Either merge the bot pull requests one at a time as they come in, or resolve the conflict in the browser:

1. Click **Resolve conflicts**.
2. Keep both entries and delete the `<<<<<<<`, `=======` and `>>>>>>>` lines.
3. Click **Mark as resolved**, then **Commit merge**.

## The @signoff assistant does not answer

- `@signoff` must be written in a new issue or in a comment by a person. It does not work in a pull request.
- Check the run of the Signoff-Assistant workflow under *Actions*.
- If the assistant asks a question, answer in a new comment that starts with `@signoff`.
- If you wrote `@signoff` by accident, the assistant replies and asks what to record. Close the issue.

If the form is easier, use **Issues → New issue → Signoff: declare or attest files**, which involves no AI. See [Declaring existing files with @signoff](usage/signoff-requests.md).

## Editing creates a fork instead of a branch

If the browser editor has no option to create a branch and a fork appears, the person has no write access to the repository yet, for example because the invitation was not accepted. Give them write access first.
