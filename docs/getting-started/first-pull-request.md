# Your first pull request

This page walks through a complete change in the browser: edit a file, open a pull request, watch the checks fail on the unfilled AI declaration, tick the declaration, and merge. You need a GitHub account with write access to the repository. No command line is involved.

The repository must already be set up as described in [Setting up the repository on GitHub](setup-on-github.md). In particular, merge commits must be allowed with the default message **Pull request title and description**, otherwise the declaration you tick never reaches `main`.

## What you will see

Two checks run on every pull request into `main`:

- **PR-signoff** validates the AI declaration ticked in the pull request description.
- **File-signoff** runs aisignoff and checks that every file (with `[history]` enabled, every line) is declared and meets the policy.

With the template untouched, both fail. After you tick the declaration, they turn green without a new push.

## 1. Change a file and open a pull request

1. Open [`docs/notes.md`](../../docs/notes.md) in the repository and click the **pencil** (Edit this file).
2. Add a line, for example `Hello from my first pull request.`
3. Click **Commit changes…**. In the dialog:
    - write a short message, for example `Add a hello line`;
    - choose **Create a new branch for this commit and start a pull request** and give the branch a name such as `demo/hello`;
    - click **Propose changes**.
4. On the "Open a pull request" page, the description is already filled with the template. It ends with the AI declaration. Leave it as it is and click **Create pull request**.

!!! note
    If the dialog has no option to create a branch and a fork appears instead, you do not have write access to the repository yet.

## 2. Watch the checks fail

Scroll down to the checks. After a few seconds **PR-signoff** and **File-signoff** turn red. Click **Details** on one of them. The message says that no generation or human review level is ticked: the template still contains its unfilled state.

This is expected. The checks ask one question: did you say how this change was made and how you checked it?

## 3. Tick the declaration

Scroll back to the description. You can tick the boxes right there, without opening an editor. For a line you typed yourself and read through:

| Part | Tick |
|---|---|
| Generation (exactly one) | **G0**: you wrote it yourself, no AI |
| AI models | none (not needed for G0) |
| Human review | **H2**: you read every line you changed |
| AI review | **A0**, or nothing (nothing ticked means A0) |
| `AI-Review-Findings:` | leave empty; it matters only for A2 and A3 |

If an AI tool helped, tick **G1** or **G2** instead and tick the model you used (or **Other:** and write its name). The [declaration levels](../concepts/declaration-levels.md) page explains what each level means.

Ticking a box edits the description, and the description check reruns on its own. After about half a minute both checks are green, and the labels `ai:G0`, `human:H2` and `ai-review:A0` appear on the right.

## 4. Make it fail on purpose

Untick **H2** and tick **H0** only. The checks go red again with a policy failure: this repository requires at least **H1** for every file. Other mistakes that fail the same way:

- ticking two generation boxes (for example G1 and G2) is an error, because exactly one is allowed;
- ticking G1 to G3 without naming a model.

Read the message under **Details** each time, then restore the correct ticks.

## 5. Merge

1. Click **Merge pull request**, then **Confirm merge**. Use a merge commit; this is the repository's configured merge method.
2. When GitHub offers it, click **Delete branch**.
3. Open **Commits** on `main`. The newest commit is the merge, and its message contains the ticked declaration. That is how the declaration stays with the files.

!!! note
    The merge commit's author is the reviewer recorded for the lines you added: whoever clicked **Merge**.

## Next steps

- To see the effect of your merge locally, see [Running aisignoff locally](local-commands.md).
- For the details of filling the template, see [Declaring a pull request](../usage/declaring-a-pull-request.md).
