# Contributing

This is a training repository. These are the conventions the exercises use, and a sensible starting point for a small team.

## Workflow

1. Pick or open an issue.
2. Branch from `main`: `git switch -c <type>/<short-description>` (for example `feature/log-row-count`).
3. Make one small change, commit it with a clear message and push the branch.
4. Open a pull request that links the issue (`Closes #<number>`), and say how you tested it.
5. Get one review. Resolve every conversation.
6. Merge, then delete the branch.

## Branch names

| Prefix | Use for |
| --- | --- |
| `feature/` | New work |
| `fix/` | Bug fixes |
| `docs/` | Documentation only |
| `add-notes-<name>`, `edit-nb-<name>` | The training labs in [LABS.md](LABS.md) |

## Before you open a pull request

```shell
python scripts/validate.py
```

It checks JSON files, Python code, saved notebook outputs, files that must not be committed, and obvious secrets. The same check runs on every pull request.

## What belongs here

Code and definitions: notebooks, pipeline definitions, SQL, documentation. Not data, credentials or connection strings. See `.gitignore`.
