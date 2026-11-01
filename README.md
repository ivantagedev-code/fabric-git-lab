# fabric-git-lab

Sample repository for a GitHub for data teams training.

The `fabric/` folder is laid out the way Fabric Git integration stores items:
one folder per item, named `<name>.<Type>`, with a `.platform` metadata file
and the item's definition files.

This is a hand-built teaching sample, not an export from a live workspace.

- `fabric/` : sample Lakehouse, notebook and data pipeline definitions
- `docs/lab-notes/` : Lab 1 notes go here
- `docs/example.ipynb` : a raw .ipynb, to compare with the readable notebook source
- `.github/CODEOWNERS` : maps folders to reviewers
- [LABS.md](LABS.md) : the exercises, with the matching training manual page for each

## Getting started

Please do this before the session. It takes about 15 minutes and means the labs start on time.
Background reading: [Getting Ready for Class](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class) in the GitHub Training Manual.

### 1. GitHub account

1. Make sure you can sign in to GitHub with the account you will use on the day.
2. Make sure you can open this repository: `https://github.com/ryanpjbyrne/fabric-git-lab`.
3. If your account is managed by your organisation (for example an Enterprise Managed User account),
   it may not be able to contribute to repositories outside your organisation. Tell the trainer before the
   session if you can open the repository but cannot push or open a pull request.

### 2. Git

1. Check whether Git is installed: `git --version`
2. If not, install it from <https://git-scm.com/downloads>. On Windows, version 2.29.2 or later is recommended.
   Git for Windows includes Git Bash and Git Credential Manager.
3. Set your identity. It is stamped on every commit you make:

   ```shell
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

### 3. A text editor

Any editor works. [Visual Studio Code](https://code.visualstudio.com) is a good default. Confirm you can open a file from the command line, for example `code .`

### 4. GitHub CLI (optional)

Useful for authentication and for opening pull requests from a terminal.
Install from <https://cli.github.com>, then check with `gh --version`.

### 5. Test that you can clone and sign in

Use HTTPS rather than SSH, because many corporate networks block SSH.

```shell
git clone https://github.com/ryanpjbyrne/fabric-git-lab.git
cd fabric-git-lab
git status
```

- When you push for the first time, Git Credential Manager normally opens a browser sign-in window.
- If you are asked for a password and it fails, you need a personal access token instead. See
  [Personal Access Tokens](https://githubtraining.github.io/training-manual/#/20_personal_access_token).
- If clone or push still fails, work through the
  [Authentication Troubleshooting Guide](https://githubtraining.github.io/training-manual/#/app_authentication).

If your organisation uses a proxy, set it once:

```shell
git config --global http.proxy http://YOUR.PROXY.SERVER:8080
```

### You are ready if

- [ ] `git --version` prints a version
- [ ] `git config --global user.name` and `user.email` show your details
- [ ] You can open the repository in a browser
- [ ] `git clone` worked and you have a `fabric-git-lab` folder
- [ ] You can open the folder in your editor

Then follow [LABS.md](LABS.md) on the day.
