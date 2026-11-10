# Git basics

The handful of commands you'll use every week. Deeper stuff comes in Week 13.

## First-time setup

Full walkthrough for WSL2 · Ubuntu 24.04 (git config, SSH key, first push): **[github-setup-wsl.md](github-setup-wsl.md)**

Short version, once that's done:

```bash
git init
git add .
git commit -m "start learning hub"
git remote add origin git@github.com:<github-user>/learning-hub.git
git push -u origin main
```

## Every review

```bash
git status            # what changed?
git add .             # stage everything
git commit -m "week 3 review"
git push
```

## Looking back

```bash
git log --oneline            # short history
git log --oneline -- weeks/  # history of just the week notes
git diff                     # unstaged changes
git diff --staged            # staged changes
```

## Oops

```bash
git restore <file>           # throw away changes to a file (careful: gone for good)
git restore --staged <file>  # unstage, keep the changes
git commit --amend           # fix the last commit message (before pushing)
```

## Good commit messages

- Short, present tense: `add hours.py table output`, not `stuff`
- One logical change per commit when you can
