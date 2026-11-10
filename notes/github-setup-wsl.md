# GitHub setup on WSL2 · Ubuntu 24.04

Takes about 45–60 minutes the first time. Do the steps in order; each one ends with a quick check.
Placeholders: `<github-user>` is your GitHub username, `<win-user>` is your Windows user folder name.

---

## 0 · Before you start (on github.com)

1. Have a GitHub account (or create one at [github.com/signup](https://github.com/signup)).
2. **Keep your email private:** *Settings → Emails* → tick **Keep my email addresses private**. Copy the address it shows, something like `12345678+<github-user>@users.noreply.github.com`.
   This goes into your commits instead of your personal email. Every commit in a public repo shows its author email, forever.

---

## 1 · Update Ubuntu and install the tools

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git unzip python3-venv python3-pip build-essential cmake gdb
```

**Check:**

```bash
git --version && python3 --version && g++ --version | head -1 && cmake --version | head -1
```

Python should show 3.12.x on 24.04.

> **Ubuntu 24.04 gotcha:** `pip install something` outside a virtual environment fails with *externally-managed-environment*. That's on purpose. Always make a venv first (`python3 -m venv .venv && source .venv/bin/activate`), then pip works normally.

---

## 2 · Put the hub in your Linux home, not on C:

Keep git repos on the Linux side (`~/…`), not under `/mnt/c/…`. It's much faster, and you avoid odd permission and line-ending problems.

```bash
ls /mnt/c/Users/                       # find your Windows user folder name
cp /mnt/c/Users/<win-user>/Downloads/learning-hub.zip ~/
cd ~ && unzip learning-hub.zip && rm learning-hub.zip
cd ~/learning-hub && ls
```

**Check:** you see `README.md ROADMAP.md SCHEDULE.md …`

To see the folder from Windows, run `explorer.exe .` inside it, or go to `\\wsl.localhost\Ubuntu-24.04\home\<linux-user>\learning-hub` in Explorer.

---

## 3 · Bring in the Python and C++ files you already have

Find them first (this lists source files in your Linux home, skipping the hub and hidden folders):

```bash
find ~ -maxdepth 4 \( -name "*.py" -o -name "*.cpp" -o -name "*.hpp" -o -name "*.h" \) \
     -not -path "*/learning-hub/*" -not -path "*/.*"
```

If they're on the Windows side instead, look under `/mnt/c/Users/<win-user>/…`.

Copy them in. Copy rather than move, and delete the originals only after the first push works:

```bash
mkdir -p ~/learning-hub/practice/python/refresh ~/learning-hub/practice/cpp/refresh
cp -r /path/to/your/python/files/. ~/learning-hub/practice/python/refresh/
cp -r /path/to/your/cpp/files/.    ~/learning-hub/practice/cpp/refresh/
```

**Before anything gets committed**, look through what you copied:

- **Compiled programs:** `.gitignore` already skips `build/`, `*.o`, `a.out` and `.venv/`. Other binaries (e.g. a `./main` you compiled) it won't. List them with `find practice -type f -executable -not -name "*.py" -not -name "*.sh"` and delete them.
- **Old git folders:** if your files were already in a git repo, the copy brings a hidden `.git` folder along, and git will treat it as a repo inside a repo. Check with `find practice -name .git` and delete what it finds (`rm -rf practice/…/.git`). Keep the original folder if you want that history.
- **Anything from work:** leave it out. This repo is public.
- **Secrets:** passwords, tokens, IP addresses or hostnames inside scripts. Remove them.

---

## 4 · Configure git

```bash
git config --global user.name  "Your Name"
git config --global user.email "12345678+<github-user>@users.noreply.github.com"   # from step 0
git config --global init.defaultBranch main
git config --global core.autocrlf input     # always commit Linux line endings, even if a Windows editor adds CRLF
git config --global pull.rebase false
git config --global core.editor nano        # or vim, if you prefer
```

**Check:** `git config --global --list`

---

## 5 · Create an SSH key and give it to GitHub

SSH means no passwords or tokens on every push, and it's good practice for Week 12 (ssh) anyway.

```bash
ssh-keygen -t ed25519 -C "wsl-ubuntu-24.04"
# Enter = default location (~/.ssh/id_ed25519)
# Passphrase: optional. Safer with one. See step 9 so you only type it once per session.

cat ~/.ssh/id_ed25519.pub
```

Copy the whole line that starts with `ssh-ed25519` (the **.pub** file, never the other one).
On GitHub: *Settings → SSH and GPG keys → New SSH key* → Title `WSL Ubuntu 24.04`, Key type **Authentication** → paste → *Add*.

**Check:**

```bash
ssh -T git@github.com
```

The first time, it asks whether to trust GitHub's host key. Compare the fingerprint with [GitHub's published fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints), then type `yes`.
Success looks like: `Hi <github-user>! You've successfully authenticated, but GitHub does not provide shell access.`

---

## 6 · Create the empty repo on GitHub

github.com → **+** → *New repository*:

- Name: `learning-hub`
- Public
- **Don't** add a README, .gitignore or license. The repo has to be empty, because your local one already has all that.

Create it, and keep the page open: it shows the SSH address `git@github.com:<github-user>/learning-hub.git`.

---

## 7 · First commit and push

```bash
cd ~/learning-hub
git init
git add .
git status            # read this list: anything that shouldn't be public? Remove it now.
git commit -m "start learning hub"
git remote add origin git@github.com:<github-user>/learning-hub.git
git push -u origin main
```

**Check:** refresh the GitHub page. The README now shows as your hub's home page, with the *Right now* box and the phase table.

After this, a normal week is just:

```bash
git add . && git commit -m "week 1 review" && git push
```

---

## 8 · Editor: VS Code connected to WSL

1. Install [VS Code](https://code.visualstudio.com/) on Windows, then the **WSL** extension (by Microsoft).
2. In the Ubuntu terminal: `cd ~/learning-hub && code .`
3. The bottom-left corner should say **WSL: Ubuntu-24.04**. You're now editing the Linux files directly, and the built-in terminal is your Ubuntu shell.
4. Inside that WSL window, install: **Python**, **C/C++**, **CMake Tools**. Markdown preview is built in (`Ctrl+Shift+V`).

VS Code's *Source Control* panel (`Ctrl+Shift+G`) shows changes and can commit/push. Still use the terminal commands for the first few weeks, though, so you learn what's happening.

**Obsidian?** It runs on Windows and can open `\\wsl.localhost\Ubuntu-24.04\home\<linux-user>\learning-hub` as a vault. It works, but it may not notice changes made from the terminal straight away. Use VS Code day to day; Obsidian is nice for reading and linking notes if you like it.

---

## 9 · Optional, but nice

**Type the SSH passphrase only once per session** (if you set one):

```bash
sudo apt install -y keychain
echo 'eval "$(keychain --eval --quiet id_ed25519)"' >> ~/.bashrc
source ~/.bashrc
```

**GitHub CLI**: create repos and check things from the terminal:

```bash
sudo apt install -y gh        # Ubuntu's version; GitHub's own apt repo has the newest
gh auth login                 # GitHub.com → SSH → use the key you made → login with browser
gh repo view --web            # opens the hub on GitHub
```

Newest-version install instructions: [cli/cli Linux install guide](https://github.com/cli/cli/blob/trunk/docs/install_linux.md).

---

## 10 · Check everything in one go

```bash
cd ~/learning-hub
bash practice/bash/check_env.sh
```

Every line should be a ✓. Anything with ✗ tells you what to fix.

---

## When something goes wrong

| Message | What it means → fix |
|---|---|
| `Permission denied (publickey)` | GitHub doesn't know this key. Check you pasted the `.pub` line in step 5; debug with `ssh -vT git@github.com` |
| `ssh: connect to host github.com port 22: Connection timed out` | The network blocks port 22 (common on office/hotel Wi-Fi). Use port 443: see below |
| `error: src refspec main does not match any` | Nothing committed yet, or the branch is called `master` → commit first, or `git branch -M main` |
| `error: remote origin already exists` | `git remote set-url origin git@github.com:<github-user>/learning-hub.git` |
| `! [rejected] main -> main (fetch first)` | The GitHub repo isn't empty (README was ticked). Easiest: delete that repo on GitHub, recreate it empty, push again |
| git is slow, or every file shows as changed | You're under `/mnt/c/…`. Move the repo to `~/` (step 2) |
| `externally-managed-environment` on `pip install` | Activate a venv first (step 1 note) |

**SSH over port 443**: add this to `~/.ssh/config` (create the file if needed), then `ssh -T git@github.com` again. See [GitHub's docs](https://docs.github.com/en/authentication/troubleshooting-ssh/using-ssh-over-the-https-port).

```
Host github.com
    Hostname ssh.github.com
    Port 443
    User git
```

---

Daily commands: [git-basics.md](git-basics.md)
