[← Overview](README.md) · **1 The mental model** · [2 Live demo →](02-live-demo.md)

# 1 · The mental model

Five words are enough to work on GitHub. You already know the ideas behind them from shared folders and
"paper_final_v3_really_final.docx".

| Word | Think of it as | Here |
|---|---|---|
| **Repository** (repo) | A shared project folder that remembers every version of every file | This page lives in one |
| **Commit** | One saved version, with a short note of what changed and who changed it | [The history of this repo](https://github.com/industrial-mathematics-group/aisignoff-playground/commits/main) |
| **Branch** | Your own copy of the folder to work in, without disturbing anyone | `main` is the official version |
| **Pull request** (PR) | "Please take my changes into `main`": the change, a discussion, and automatic checks | [A merged one](https://github.com/industrial-mathematics-group/aisignoff-playground/pull/13) |
| **Merge** | The changes go into `main`; the pull request is closed | The green button |

Two more you'll meet: an **issue** is a note or a request ("this figure is wrong", "please record …"), and a
**release** is a named, frozen version of the whole repository, such as the one you publish with a paper.

## The picture

Everyone works on their own branch. A pull request brings one branch back into `main`.

```mermaid
gitGraph
    commit id: "data added"
    commit id: "figure 1"
    branch jane/new-figure
    checkout jane/new-figure
    commit id: "figure 2 draft"
    commit id: "caption fixed"
    checkout main
    branch omar/typos
    checkout omar/typos
    commit id: "typos in notes"
    checkout main
    merge omar/typos id: "PR #15 merged"
    merge jane/new-figure id: "PR #14 merged"
    commit id: "release v1.0" tag: "v1.0"
```

## What happens to a change

```mermaid
flowchart LR
    A["Edit or upload<br/>a file"] --> B["Save it on a<br/>new branch"]
    B --> C["Open a<br/>pull request"]
    C --> D{"Checks"}
    D -- "red: something's missing" --> E["Fix it, e.g.<br/>tick the boxes"]
    E --> D
    D -- green --> F["Merge into main"]
    F --> G["Part of the<br/>history for good"]
```

The checks are little robots that run on every pull request. In this repository they ask one question:
**did you say how this change was made and how you checked it?** That's AI signoff, part 3.

## Why bother?

- **Nothing is lost.** Every version of every file is kept, with who changed it, when and why.
- **Nobody overwrites anybody.** Everyone works on a branch; `main` changes only through pull requests.
- **Review happens in one place.** Comments, checks and the decision to merge sit next to the change.
- **It's citable.** A release can get a DOI from Zenodo (part 5), so the exact files behind a paper stay findable.

> It works the same for code, LaTeX, figures, CSV files and slides. GitHub shows the differences line by line
> for text files, and the old and the new version side by side for images. Other files, such as PDFs or Word
> documents, are kept and versioned just the same, but GitHub can't show what changed inside them.

---

[← Overview](README.md) · [2 Live demo →](02-live-demo.md)
