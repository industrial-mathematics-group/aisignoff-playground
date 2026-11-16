# Declaring existing files with @signoff

Files that are already in `main` can be declared, or their review recorded, without editing `SIGNOFF.toml` by hand. You describe what to record in an issue, and a bot opens a pull request that changes `SIGNOFF.toml`.

## When to use it

Declarations for new or changed files come from the ticked pull request template; see [Declaring a pull request](declaring-a-pull-request.md). Use a signoff request when the files are already in `main` and you want to:

- declare how they were made, or
- record that someone reviewed them, for example a line-by-line read-through.

The declarations are written to [`SIGNOFF.toml`](../reference/signoff-toml.md). Which workflows handle the request is described under [workflows](../deploy-extend/workflows.md): `signoff-request.yml` for the issue form and `signoff-assistant.yml` for the assistant.

## Option 1: the @signoff assistant

1. Open **Issues → New issue → Blank issue**, or comment in an open issue.
2. Write `@signoff` and describe in your own words what to record, as you would to a colleague. For example:

    > @signoff I checked `results/summary.md` line by line against `results/fit.csv` today. Please record a human review of H2 with me, Jane Doe, as reviewer.

3. The **signoff assistant** (an AI) answers with what it understood, or asks what is missing. Answer in a new comment that starts with `@signoff`.
4. The **signoff bot** opens a pull request that changes `SIGNOFF.toml`.

!!! note
    `@signoff` must be in a new issue or in a comment by a person. It is not picked up in pull requests.

## Option 2: the issue form

If you prefer a form to a chat, use **Issues → New issue → Signoff: declare or attest files**. It asks the same questions as drop-down fields, and no AI is involved. It ends the same way: a pull request that changes `SIGNOFF.toml`.

## Attestations, such as H3

When the request records a review of files as they are now, the bot adds an attestation to `SIGNOFF.toml`. An attestation names a path and the blob (the exact file content) it applies to, together with the review level and the reviewer. This repository has one:

```toml
[[attestations]]
path = "docs/notes.md"
blob = "60eb1495fe2f5be7a4c26c1dc013b9c5ac4bb87b"
Human-Review = "H3"
Reviewed-by = ["John Doe"]
```

H3 means the change was independently validated. A second person's line-by-line review is one way to get there; the author cannot give themselves H3 by rereading. See [declaration levels](../concepts/declaration-levels.md) for the full scale.

## Who ticks the resulting pull request

The bot's pull request has the usual declaration template. **The person who made the request ticks the boxes**, in particular their human review of the bot's change:

1. Open the pull request and check **Files changed**. It should contain only the entries you asked for, with the names you gave.
2. Tick your human review in the description. Did the bot write down what you said? That decision is yours, even though a bot made the change.
3. Wait for the checks to turn green, then merge.

The bot may name you in the description (`Responsible person: @you`). You remain responsible for the change, whoever or whatever wrote it.

## Several requests at once

If several signoff requests are open at the same time, their pull requests all add entries at the end of `SIGNOFF.toml`, and the later ones can show merge conflicts. See [Troubleshooting](../troubleshooting.md) for how to resolve this, or merge the bot pull requests one at a time.
