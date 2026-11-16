# Inline tags and commit message trailers

Declarations can be written as "Key: value" lines in a commit message. This page lists the keys, shows how the playground uses them, and explains why the header comment in `scripts/make_results.py` no longer counts.

## The keys

A declaration is a set of "Key: value" lines, one per line. The README names these six:

| Key | Declares |
|---|---|
| `AI-Generation` | Generation level, for example `G2` |
| `Assisted-by` | The AI model or tool that helped |
| `Human-Review` | Human review level, for example `H1` |
| `Reviewed-by` | The person who reviewed |
| `AI-Review` | AI review level, for example `A1` |
| `AI-Reviewed-by` | The AI model that reviewed |

The levels are explained in [declaration levels](../concepts/declaration-levels.md).

## In a commit message

Put the lines in the message of a commit that lands on `main`. With `[history]` enabled in `SIGNOFF.toml`, each line takes the declaration of the commit that landed it, so the lines this commit adds are declared by these keys.

```text
Update the notes

AI-Generation: G2
Assisted-by: Claude Opus
Human-Review: H1
Reviewed-by: Jane Doe
AI-Review: A1
AI-Reviewed-by: Claude Opus, fresh session
```

Lines you do not declare in a commit take the file-level declaration from `SIGNOFF.toml`.

### Effect on a plain push

Scenario 1 in the README tries this. A commit pushed to `main` with a plain message declares nothing, so its new lines take the file-level declaration (G0 · H2 · A0 in this repository). With "Key: value" lines such as `AI-Generation: G2` in the message, `aisignoff report --files` shows the file partly at G2. See [scenarios](scenarios.md).

### Merge and squash commits

With the repository's default commit message set to **Pull request title and description**, the ticked pull request template becomes the merge or squash commit message, and aisignoff reads it as these same keys. See [line-level history](../concepts/line-level-history.md) and [setting up the repository](../getting-started/setup-on-github.md).

With `merge-method = "merge"`, a branch commit that carries `AI-Generation: G3` raises the generation of the lines it wrote. With `merge-method = "squash"`, the squash commit's description declares all its lines and the generation of the branch commits is ignored.

## Header comments in files

Files used to declare themselves with the same keys as a comment at the top. `scripts/make_results.py` still starts with such a header:

```python
# AI-Generation: G1
# Human-Review: H2
# AI-Review: A1
# Assisted-by: Claude Opus 5.5 (Anthropic)
# AI-Reviewed-by: Claude Opus 5.5 (Anthropic), self-check by the generating session
# Reviewed-by: Pascal Jung
```

!!! note
    From aisignoff 1.0.0rc7 on, this header comment no longer counts as a declaration. The playground keeps the levels the tags used to give in `SIGNOFF.snapshot.json`, as an entry with the source `inline`: G1 · H2 · A0, assisted by Claude Opus 5.5, reviewed by Pascal Jung. The README declares the file as G1 · H2 · A0 for that reason.

Do not rely on a header comment to declare a file. Use an annotation in `SIGNOFF.toml`, or declare the lines through the pull request or commit that lands them. For frozen declarations see [snapshots and freezing](../concepts/snapshots-and-freeze.md); for the full list of sources see [where declarations live](../concepts/where-declarations-live.md).
