# Where declarations are kept

Every file in this repository needs a declaration of how it was made and checked (see [declaration levels](declaration-levels.md)). The declaration can come from several places. This page lists them, explains which one wins when more than one applies, and shows what this repository declares for each path.

## The sources

| Source | Where it is written | What it covers |
|---|---|---|
| Annotations | `[[annotations]]` in `SIGNOFF.toml` | Files that match a path pattern |
| Inline tags | `Key: value` lines in the file itself | That one file |
| Commit and pull request descriptions | The ticked pull request template, or `Key: value` lines in the merge or squash commit message | The lines that commit landed on `main` |
| Attestations | `[[attestations]]` in `SIGNOFF.toml` | One specific version of a file, identified by its blob |
| Per-commit entries | `[[commits]]` in `SIGNOFF.toml` | The lines of one commit |

### Annotations

An annotation gives a `path` pattern and the declaration fields: `AI-Generation`, `Human-Review`, `AI-Review`, and optionally `Assisted-by`, `Reviewed-by` and `AI-Reviewed-by`.

```toml
[[annotations]]
path = "src/playground/fitting.py"
AI-Generation = "G2"
Human-Review = "H1"
AI-Review = "A0"
Assisted-by = ["Claude Opus 5.5 (Anthropic)"]
Reviewed-by = ["Pascal Jung"]
```

The pattern `**` matches every file, so an annotation with `path = "**"` acts as the default for the whole repository.

### Inline tags

A file can carry its own declaration as tags in the file. Inline tags win over `SIGNOFF.toml` unless the matching annotation sets `precedence = "override"`.

!!! note
    `scripts/make_results.py` still has a header comment with tags. From aisignoff 1.0.0rc7 on, that comment no longer counts. The levels it declared are kept in `SIGNOFF.snapshot.json`. See [inline tags and commit trailers](../usage/inline-tags-and-commit-trailers.md).

### Commit and pull request descriptions

With line-level declarations switched on (`[history]` in `SIGNOFF.toml`), each line takes the declaration of the commit that landed it on `main`. That declaration is the ticked pull request template or the `Key: value` lines in the merge or squash commit message. For this to work, the repository's default merge commit message must be **Pull request title and description**; see [setting up the repository](../getting-started/setup-on-github.md). The details are on the [line-level history](line-level-history.md) page.

### Attestations

An attestation records a human review of a specific version of a file. It names the `path` and the `blob` (the git object id of the file content) and gives the review fields. This repository has one:

```toml
[[attestations]]
path = "docs/notes.md"
blob = "60eb1495fe2f5be7a4c26c1dc013b9c5ac4bb87b"
Human-Review = "H3"
Reviewed-by = ["John Doe"]
```

Because it is tied to a blob, the attestation applies only while the file has exactly that content. You normally don't write attestations by hand; the [@signoff assistant and the issue form](../usage/signoff-requests.md) open a pull request that adds them.

### Per-commit entries

A `[[commits]]` entry declares the lines that one commit introduced, identified by its `commit` hash. It is for commits whose own message declared nothing. This repository has two:

```toml
[[commits]]
commit = "2c89617"
AI-Generation = "G1"
Assisted-by = ["Claude Sonnet 5.5 (Anthropic)"]
Human-Review = "H2"
Reviewed-by = ["Pascal Jung"]
AI-Review = "A0"
```

The second entry, for commit `a24781b`, declares G1 with an A3 AI review by a different model.

## Precedence

1. **The last annotation that matches a file wins.** Annotations are read in order, so put general patterns first and specific ones after them. That is why the `**` default is at the top of `SIGNOFF.toml`.
2. **Inline tags win over `SIGNOFF.toml`**, unless the matching annotation sets `precedence = "override"`.
3. **With `[history]` enabled**, a line takes the declaration of the commit that landed it. The annotations are the fallback for lines whose commit declares nothing.

## What this repository declares

| Path | Declared as | Source |
|---|---|---|
| everything (`**`) | G0 · H2 · A0, reviewed by Pascal Jung | default annotation |
| `src/playground/fitting.py` | G2 · H1 · A0, Claude Opus 5.5 | annotation for that file |
| `results/**` | G3 · H1 · A1, Claude Opus 5.5, with a fresh review session | annotation for the folder |
| `docs/notes.md` | H3, reviewed by John Doe | attestation for one blob |
| `scripts/make_results.py` | G1 · H2 · A0, Claude Opus 5.5 | its former inline tags, kept in `SIGNOFF.snapshot.json` |

Files that match only the `**` annotation, such as `src/playground/stats.py`, take G0 · H2 · A0. Lines landed by a pull request or commit that declares its own levels take those levels instead; see [line-level history](line-level-history.md) and [snapshots and freezing](snapshots-and-freeze.md) for lines whose levels have been frozen.
