# Running the workshop

The `workshop/` folder holds the material for a 75-minute introduction to GitHub and AI signoff, held on 19 November 2026. Everything is done in the web browser, with no command line. This page describes what the folder contains and what a facilitator has to prepare before the session.

## What the folder contains

| Path | Content |
|---|---|
| `workshop/README.md` | Overview, schedule, preparation for participants and ground rules |
| `workshop/01-mental-model.md` | Repository, commit, branch, pull request and merge, shown as diagrams |
| `workshop/02-live-demo.md` | Live demo: change a file, open a pull request, see the checks go red and green, merge |
| `workshop/03-aisignoff.md` | Why AI use is declared, the G, H and A levels, responsibility, @signoff, the report |
| `workshop/04-hands-on.md` | Three exercises, plus an optional upload exercise |
| `workshop/05-zenodo.md` | Releases and DOIs with Zenodo |
| `workshop/cheat-sheet.md`, `cheat-sheet.html`, `cheat-sheet.pdf` | One-page take-home summary, as Markdown, HTML and printable PDF |
| `workshop/facilitator-notes.md` | Checklist, timing and troubleshooting for the person running the session |
| `workshop/hands-on/` | One file per participant, plus `example-person.md` as a model |

Participants do not need the facilitator notes.

## The five parts

| Part | Page | Time | What happens |
|---|---|---|---|
| 1 | The mental model | 10 min | Repository, commit, branch, pull request and merge as pictures |
| 2 | Live demo | 20 min | Edit a file in the browser, open a pull request, watch the checks fail and pass, merge |
| 3 | AI signoff | 15 min | The G, H and A levels, who is responsible, the @signoff assistant, the report |
| 4 | Hands-on | 20 min | Everyone adds a file, declares it in a pull request and merges it |
| 5 | Releases and DOIs | 10 min | Zenodo gives every GitHub release a DOI, a badge and a citation |

The facilitator notes suggest this timing: part 1 at 0:00, part 2 at 0:10, part 3 at 0:30, part 4 at 0:45, part 5 at 1:05, and questions at 1:15, when the cheat sheet is handed out.

If time runs short, drop the optional upload and exercise 2. Keep exercise 3: it is the only place where participants use @signoff themselves.

## The hands-on folder

Each participant adds one file to `workshop/hands-on/`, named after themselves in lower case with hyphens (`jane-doe.md`), in their own pull request. This way nobody edits the same file as anybody else.

The exercises are:

1. **Your first pull request.** Create the file, open a pull request, tick the AI declaration and merge.
2. **Break it on purpose.** Try two generation boxes, G1 without a model, and only H0, and read why each check is red.
3. **Review your neighbour with @signoff.** Open an issue that starts with `@signoff`, describe the review in words, and tick the human review in the pull request the bot opens. Exercise 3 needs the neighbour's exercise 1 to be merged first.

The repository is public, so participants should only put things in their files that they are happy to have on the internet.

## What to prepare

### Access

- Collect each participant's GitHub user name and give them **Write** access to the repository. An organisation team with Write access is the easiest to clean up afterwards.
- Write access matters. Without it, the browser silently creates a fork for each edit, and the signoff bot only opens pull requests for people who can push.
- Ask participants to accept the invitation before the session. It arrives by e-mail and expires after 7 days.

### Repository settings

In *Settings*:

- *General → Pull Requests*: allow merge commits, and set their default message to **Pull request title and description**. Otherwise the ticked declaration never reaches `main`. See [Setting up the repository on GitHub](../getting-started/setup-on-github.md).
- *General → Pull Requests*: switch on **Automatically delete head branches**, so merged branches do not pile up.
- *Rules → Rulesets* for `main`: require a pull request and the checks **PR-signoff** and **File-signoff**. Do not require approvals, so everyone can merge their own pull request.
- The signoff bot app must be installed on the repository, and the `ANTHROPIC_API_KEY` secret must be available to it, so that the @signoff assistant can answer.

### Zenodo

Decide whether part 5 shows a live demo on the [Zenodo Sandbox](https://sandbox.zenodo.org), which issues test DOIs, or a real record. A sandbox demo needs the sandbox connected to the repository beforehand. The first archive can take a few minutes, so publish a release the day before and show that. If you ever make a real release of this repository, add a `LICENSE` file first.

### Dry run

- Do the live demo once the day before, from start to end, including the deliberate H0 failure. Use a different branch name on the day.
- Print the cheat sheet (A4, one page), one per person.

## Common problems during the session

| Symptom | Cause and fix |
|---|---|
| "Commit changes" offers no new branch, and a fork appears | The person has no write access yet, usually because the invitation was not accepted |
| A check stays red after ticking | Two generation boxes, G1 to G3 without a model, only H0 (this repository requires H1), or the page was not reloaded. The check's **Details** says which |
| A check does not rerun after ticking | Reload the page. If it is still old, untick and tick one box again |
| "Merge pull request" is greyed out | The checks are still running or red, or the ruleset requires an approval |
| A second bot pull request shows "This branch has conflicts" | Several signoff requests change the end of `SIGNOFF.toml` at once. Resolve the conflict in the browser and keep both entries, or merge the bot pull requests one at a time |
| The assistant does not answer | `@signoff` must be in a new issue or in a comment by a person, not in a pull request. Check *Actions → Signoff-Assistant* |

For more, see [Troubleshooting](../troubleshooting.md).

## Afterwards

- Close leftover pull requests and issues, and delete their branches.
- The files in `workshop/hands-on/` can stay as a record, or one pull request can remove them.
- Remove the workshop team's access, or keep it for the next time.
