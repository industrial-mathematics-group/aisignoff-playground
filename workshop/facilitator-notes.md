[← Overview](README.md)

# Facilitator notes

For whoever runs the session. Participants don't need this page.

## Before Thursday

**Access**

- [ ] Collect everyone's GitHub user name and give them **Write** access to this repository (an organisation
      team with Write on `aisignoff-playground` is easiest to clean up afterwards). Write access matters:
      without it the browser silently creates a fork for every edit, and the signoff bot only opens pull
      requests for people who can push.
- [ ] Ask them to accept the invitation **before** the session (it arrives by e-mail and expires after 7 days).

**Repository settings** (*Settings*)

- [ ] *General → Pull Requests:* **Allow merge commits** is on, and its default message is **Pull request title
      and description**. Otherwise the ticked declaration never reaches `main`.
- [ ] *General → Pull Requests:* **Automatically delete head branches** on, so merged branches don't pile up.
- [ ] *Rules → Rulesets* for `main`: require a pull request and the checks **PR-signoff** and **File-signoff**.
      Don't require approvals for the workshop, so everyone can merge their own pull request.
- [ ] The signoff bot app is installed on the repository and the `ANTHROPIC_API_KEY` secret is available to it
      (the @signoff assistant last worked here in [#12](https://github.com/industrial-mathematics-group/aisignoff-playground/issues/12)).

**Zenodo** (part 5)

- [ ] Decide between a live demo on the [Zenodo Sandbox](https://sandbox.zenodo.org) (test DOIs, nothing
      permanent) and showing a real record, such as [aisignoff's](https://github.com/industrial-mathematics-group/aisignoff).
      A sandbox demo needs the sandbox connected to this repository beforehand; the first archive can take a
      few minutes, so publish one release the day before and show that.
- [ ] If you'll ever make a real release of this repository: add a `LICENSE` first.

**Dry run**

- [ ] Do the live demo once the day before, end to end, including the deliberate H0 failure. Use a different
      branch name on the day.
- [ ] Print the [cheat sheet](cheat-sheet.pdf), one per person (A4, one page).

## Timing

| Time | Part | Notes |
|---|---|---|
| 0:00 | [1 Mental model](01-mental-model.md) | Keep it to pictures. Show the commit history of this repo as the "proof" |
| 0:10 | [2 Live demo](02-live-demo.md) | Big font in the browser (Ctrl +). Narrate each click. Let the checks fail first |
| 0:30 | [3 AI signoff](03-aisignoff.md) | The levels table and "who is responsible" are the core; the rest can be skimmed |
| 0:45 | [4 Hands-on](04-hands-on.md) | Walk around. Exercise 3 needs exercise 1 merged first |
| 1:05 | [5 Releases and DOIs](05-zenodo.md) | |
| 1:15 | Questions | Hand out the cheat sheet |

If time runs short, drop the optional upload and exercise 2; keep exercise 3, since it's the only place they
use @signoff themselves.

## What tends to go wrong

| Symptom | Cause and fix |
|---|---|
| "Commit changes" has no option to create a branch, and a fork appears | The person has no write access yet (invitation not accepted) |
| A check stays red after ticking | Two generation boxes, a G1–G3 without a model, only H0 (this repo needs H1), or the page wasn't reloaded. **Details** on the check says which |
| A check doesn't rerun after ticking | Reload the page. If it's still old, untick and tick one box again |
| "Merge pull request" is greyed out | Checks still running or red, or the ruleset requires an approval |
| Two bot pull requests both change the end of `SIGNOFF.toml`: the second shows "This branch has conflicts" | Expected when several signoff requests run at once. **Resolve conflicts** in the browser: keep both entries, delete the `<<<<<<<`, `=======` and `>>>>>>>` lines, **Mark as resolved → Commit merge**. Or merge the bot pull requests one at a time as they come in |
| The assistant doesn't answer | `@signoff` must be in a new issue or a comment by a person, not in a pull request. Check *Actions → Signoff-Assistant* |
| Someone wrote `@signoff` by accident | The assistant replies and asks; close the issue |

## Afterwards

- Close leftover pull requests and issues, and delete their branches.
- The files in `workshop/hands-on/` can stay as a record, or go in one pull request that removes them.
- Remove the workshop team's access, or keep it for the next time.
