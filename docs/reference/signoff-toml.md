# SIGNOFF.toml reference

`SIGNOFF.toml` in the repository root holds the declarations that are not carried by pull requests or commits: defaults, per-path annotations, attestations and per-commit entries. This page lists every key that the file in this repository uses, with the values set here.

!!! note
    This page covers only what `SIGNOFF.toml` in this repository shows. Other keys that aisignoff may support are not listed.

## Top-level keys

| Key | Value here | Meaning |
|---|---|---|
| `version` | `4` | Version of the file format. |
| `exclude` | not set (a commented-out example) | A list of path patterns for files that need no declaration. The example in the file is `["reviews/**", "docs/build/**"]`. |

```toml
version = 4

# exclude = ["reviews/**", "docs/build/**"]
```

## `[history]`

Turns on line-level declarations: each line takes the declaration of the commit that landed it on `main`. The annotations act as the fallback for lines whose commit declares nothing.

| Key | Value here | Meaning |
|---|---|---|
| `enabled` | `true` | Switches line-level declarations on. |
| `merge-method` | `"merge"` | How pull requests land. The file names three values: `"merge"` (the default), `"squash"` and `"rebase"`. |
| `undeclared` | not set (commented out) | The commented example is `undeclared = "error"`, which requires a declaration from every commit that lands on `main`. |

```toml
[history]
enabled = true
merge-method = "merge"
# undeclared = "error"
```

## `[policy]`

Sets the minimum review levels. The comment in the file adds that G1–G3 always need at least A1.

| Key | Value here | Meaning |
|---|---|---|
| `"*"` | `{ human = "H1" }` | Every file needs at least human review H1. |
| `G3` | `{ human = "H1", ai = "A1" }` | Files at generation level G3 need at least H1 and A1. |

```toml
[policy]
"*" = { human = "H1" }
G3  = { human = "H1", ai = "A1" }
```

## `[[annotations]]`

Each `[[annotations]]` table declares the levels of the files that match `path`. The last annotation that matches a file wins. Inline tags in a file win over this file unless the matching annotation sets `precedence = "override"`.

| Key | Meaning |
|---|---|
| `path` | The file or glob the annotation applies to. |
| `precedence` | Optional. `"override"` makes the annotation win over inline tags. |

The declaration fields are listed [below](#declaration-fields).

This repository has three annotations:

| `path` | Generation | Human review | AI review |
|---|---|---|---|
| `**` | G0 | H2 | A0 |
| `src/playground/fitting.py` | G2 | H1 | A0 |
| `results/**` | G3 | H1 | A1 |

```toml
[[annotations]]
path = "**"
AI-Generation = "G0"
Human-Review = "H2"
AI-Review = "A0"
Reviewed-by = ["Pascal Jung"]

[[annotations]]
path = "src/playground/fitting.py"
AI-Generation = "G2"
Human-Review = "H1"
AI-Review = "A0"
Assisted-by = ["Claude Opus 5.5 (Anthropic)"]
Reviewed-by = ["Pascal Jung"]

[[annotations]]
path = "results/**"
AI-Generation = "G3"
Human-Review = "H1"
AI-Review = "A1"
Assisted-by = ["Claude Opus 5.5 (Anthropic)"]
Reviewed-by = ["Pascal Jung"]
AI-Reviewed-by = ["Claude Opus 5.5 (Anthropic), fresh review session"]
```

## `[[attestations]]`

An attestation records a review of one specific version of a file.

| Key | Meaning |
|---|---|
| `path` | The file that was reviewed. |
| `blob` | The git blob hash of the reviewed version of the file. |

The declaration fields (here `Human-Review` and `Reviewed-by`) follow the same names as in annotations.

This repository has one attestation:

```toml
[[attestations]]
path = "docs/notes.md"
blob = "60eb1495fe2f5be7a4c26c1dc013b9c5ac4bb87b"
Human-Review = "H3"
Reviewed-by = ["John Doe"]
```

## `[[commits]]`

A `[[commits]]` table declares the levels of one commit.

| Key | Meaning |
|---|---|
| `commit` | The commit the declaration belongs to, given as an abbreviated hash. |

The declaration fields follow.

This repository has two entries:

```toml
[[commits]]
commit = "2c89617"
AI-Generation = "G1"
Assisted-by = ["Claude Sonnet 5.5 (Anthropic)"]
Human-Review = "H2"
Reviewed-by = ["Pascal Jung"]
AI-Review = "A0"

[[commits]]
commit = "a24781b"
AI-Generation = "G1"
Assisted-by = ["Claude Opus 5.5 (Anthropic)"]
AI-Review = "A3"
AI-Reviewed-by = ["Fable 5.1, extensive review by a different model"]
```

Not every field has to be present: the second entry sets no human review.

## Declaration fields

These fields appear in annotations, attestations and commit entries.

| Field | Type | Values or content |
|---|---|---|
| `AI-Generation` | string | `G0` to `G3` |
| `Human-Review` | string | `H0` to `H3` |
| `AI-Review` | string | `A0` to `A3` |
| `Assisted-by` | list of strings | The AI models that helped generate the content. |
| `Reviewed-by` | list of strings | The people who reviewed it. |
| `AI-Reviewed-by` | list of strings | The AI models (and, in free text, the review setup) that reviewed it. |

For what the levels mean, see [declaration levels](../concepts/declaration-levels.md).
