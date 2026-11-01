# Lab guide

Hands-on exercises that use this repository. Each one links to the matching page in the
[GitHub Training Manual](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class),
which is the optional reading if you want more depth.

Manual base URL: `https://githubtraining.github.io/training-manual/#/`

| Exercise | Where you work | Manual page |
| --- | --- | --- |
| [Setup](#setup) | Terminal | [Getting Ready for Class](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class), [Local Git Configs](https://githubtraining.github.io/training-manual/#/05_local_git_configs) |
| [Lab 1a: clone and branch](#lab-1a-clone-and-branch) | Terminal | [Branching with Git](https://githubtraining.github.io/training-manual/#/04_branching_with_git), [Working Locally](https://githubtraining.github.io/training-manual/#/06_working_locally) |
| [Lab 1b: edit, commit, push](#lab-1b-edit-commit-push) | Terminal | [Working Locally](https://githubtraining.github.io/training-manual/#/06_working_locally), [Local History](https://githubtraining.github.io/training-manual/#/10_local_history) |
| [Lab 2: pull request and review](#lab-2-pull-request-and-review) | GitHub | [Collaborating on Code](https://githubtraining.github.io/training-manual/#/07_collaborating_on_code), [Merging Pull Requests](https://githubtraining.github.io/training-manual/#/09_merging_pull_requests) |
| [Demo: protect main and add CODEOWNERS](#demo-protect-main-and-add-codeowners) | GitHub | [Protected Branches & CODEOWNERS](https://githubtraining.github.io/training-manual/#/17_protected_branches) |
| [Lab 4: create and resolve a merge conflict](#lab-4-create-and-resolve-a-merge-conflict) | GitHub and terminal | [What is a merge conflict](https://githubtraining.github.io/training-manual/#/12a_what_is_a_merge_conflict), [Resolving merge conflicts](https://githubtraining.github.io/training-manual/#/12b_resolving_merge_conflicts) |
| [Revert a commit](#revert-a-commit) | Terminal | [Reverting Commits](https://githubtraining.github.io/training-manual/#/15_reverting_commits) |

Related reading that has no lab in this repository:

- Sign-in and tokens: [Personal Access Tokens](https://githubtraining.github.io/training-manual/#/20_personal_access_token), [Authentication Troubleshooting Guide](https://githubtraining.github.io/training-manual/#/app_authentication)
- Keeping files out of the repo: [.gitignore File](https://githubtraining.github.io/training-manual/#/23_gitignore)
- Automation: [GitHub Actions](https://githubtraining.github.io/training-manual/#/17_github_actions)
- Everyday commands: [Helpful Git Commands](https://githubtraining.github.io/training-manual/#/16_helpful_git_commands)

## Setup

Manual: [Getting Ready for Class](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class), [Local Git Configs](https://githubtraining.github.io/training-manual/#/05_local_git_configs)

1. Check you can sign in to GitHub and open this repository.
2. Install Git and confirm it works: `git --version`.
3. Set your identity (used on every commit you make):

   ```shell
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

## Lab 1a: clone and branch

Manual: [Branching with Git](https://githubtraining.github.io/training-manual/#/04_branching_with_git), [Working Locally](https://githubtraining.github.io/training-manual/#/06_working_locally)

1. Clone the repository: `git clone <REPO-URL>`, then `cd fabric-git-lab`.
2. Look around: `git status` and `git log --oneline`.
3. Create your own branch and switch to it: `git switch -c lab1/<your-name>`.
4. Confirm where you are: `git branch`.

## Lab 1b: edit, commit, push

Manual: [Working Locally](https://githubtraining.github.io/training-manual/#/06_working_locally), [Local History](https://githubtraining.github.io/training-manual/#/10_local_history)

Each person edits a different file, so nobody clashes yet.

1. Create your own file: `docs/lab-notes/<your-name>.md`, with a line or two about what you want from the day.
2. Check what changed: `git status`.
3. Stage it: `git add docs/lab-notes/<your-name>.md`.
4. Commit it: `git commit -m "Add <your-name> lab notes"`.
5. Push your branch: `git push -u origin lab1/<your-name>`.
6. If the push is rejected for sign-in reasons, see the
   [Authentication Troubleshooting Guide](https://githubtraining.github.io/training-manual/#/app_authentication).

## Lab 2: pull request and review

Manual: [Collaborating on Code](https://githubtraining.github.io/training-manual/#/07_collaborating_on_code), [Merging Pull Requests](https://githubtraining.github.io/training-manual/#/09_merging_pull_requests)

Work in pairs so everyone reviews and is reviewed.

1. On GitHub, open a pull request from `lab1/<your-name>` into `main`. Write a short description of the change.
2. Review your partner's pull request. On the **Files changed** tab, add a line comment, then finish the review with Comment, Approve or Request changes.
3. Respond to any comments on your own pull request.
4. Agree a merge method with the group (merge commit or squash) and merge once it is approved.
5. Delete the merged branch.

## Demo: protect main and add CODEOWNERS

Manual: [Protected Branches & CODEOWNERS](https://githubtraining.github.io/training-manual/#/17_protected_branches)

Trainer-led. Use your own copy of the repository, not the shared one.

1. In the repository settings, add a branch rule or ruleset for `main` that requires a pull request and one approval.
2. Edit `.github/CODEOWNERS` and replace the placeholder team handle with a real user or team, for example `/fabric/ @your-org/your-team`.
3. Try `git push origin main` and show it being rejected.
4. Open a pull request instead and show the required review.

## Lab 4: create and resolve a merge conflict

Manual: [What is a merge conflict](https://githubtraining.github.io/training-manual/#/12a_what_is_a_merge_conflict), [Resolving merge conflicts](https://githubtraining.github.io/training-manual/#/12b_resolving_merge_conflicts)

Two branches change the same lines of `fabric/silver_clean.Notebook/notebook-content.py`:

| Branch | Change |
| --- | --- |
| `edit-nb-A` | Strip spaces from postcodes |
| `edit-nb-B` | Trim postcodes before upper-casing |

1. Open a pull request for each branch into `main`.
2. Merge the pull request for `edit-nb-A`.
3. Open the pull request for `edit-nb-B`. GitHub now reports a conflict.
4. Resolve it: on GitHub with **Resolve conflicts**, or locally with
   `git switch edit-nb-B`, `git merge main`, edit the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), then `git add`, `git commit` and `git push`.
5. Agree what the combined result should be, then merge.

If you also want a feature branch to try the pull request flow on, `feature/log-row-count` adds a row count to the log with no conflict.

## Revert a commit

Manual: [Reverting Commits](https://githubtraining.github.io/training-manual/#/15_reverting_commits)

A commit cannot simply be deleted from shared history. Revert creates a new commit that undoes it.

1. Find the commit to undo: `git log --oneline`.
2. Revert it: `git revert <commit-id>`.
3. Push: `git push`.
4. On GitHub, merged pull requests have a **Revert** button that does the same thing through a new pull request.

## Optional: visualise it

[Visualizing Git](https://git-school.github.io/visualizing-git/) shows branches, merges and reverts as a diagram.
