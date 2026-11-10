#!/usr/bin/env bash
# check_env.sh: checks that the learning-hub setup is complete.
# Usage (from anywhere):  bash ~/learning-hub/practice/bash/check_env.sh
#
# Read through it once you reach Week 7 (bash scripting): it uses functions,
# loops, if/else, command substitution and exit codes.

fails=0
ok()   { printf '  \033[32m✓\033[0m %s\n' "$1"; }
bad()  { printf '  \033[31m✗\033[0m %s\n' "$1"; fails=$((fails + 1)); }
note() { printf '  \033[33m!\033[0m %s\n' "$1"; }

hub="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

echo "System"
if grep -qi microsoft /proc/version 2>/dev/null; then ok "running inside WSL"; else ok "native Linux"; fi
if [ -r /etc/os-release ]; then
    . /etc/os-release
    ok "${PRETTY_NAME:-unknown distro}"
fi

echo "Tools"
for cmd in git python3 g++ make cmake gdb ssh unzip; do
    if command -v "$cmd" >/dev/null 2>&1; then
        case "$cmd" in
            ssh)   ver="$(ssh -V 2>&1)" ;;
            unzip) ver="$(unzip -v 2>&1 | head -n1)" ;;
            *)     ver="$("$cmd" --version 2>&1 | head -n1)" ;;
        esac
        ok "$cmd: $ver"
    else
        bad "$cmd missing → sudo apt install -y git python3-venv build-essential cmake gdb openssh-client unzip"
    fi
done

echo "Python venv"
tmp="$(mktemp -d)"
if python3 -m venv "$tmp/venv" >/dev/null 2>&1; then
    ok "python3 -m venv works"
else
    bad "can't create a venv → sudo apt install -y python3-venv"
fi
rm -rf "$tmp"

echo "Git config"
name="$(git config --global user.name 2>/dev/null)"
email="$(git config --global user.email 2>/dev/null)"
[ -n "$name" ]  && ok "user.name = $name"   || bad "user.name not set → git config --global user.name \"Your Name\""
if [ -n "$email" ]; then
    ok "user.email = $email"
    case "$email" in
        *@users.noreply.github.com) ;;
        *) note "email isn't the GitHub noreply address; it will be public in every commit" ;;
    esac
else
    bad "user.email not set → see notes/github-setup-wsl.md step 4"
fi
[ "$(git config --global init.defaultBranch)" = "main" ] \
    && ok "default branch = main" \
    || note "init.defaultBranch isn't main → git config --global init.defaultBranch main"

echo "SSH + GitHub"
if ls "$HOME"/.ssh/id_*.pub >/dev/null 2>&1; then
    ok "SSH key found: $(ls "$HOME"/.ssh/id_*.pub | head -n1)"
else
    bad "no SSH key → ssh-keygen -t ed25519 (step 5)"
fi
gh_reply="$(ssh -T -o BatchMode=yes -o ConnectTimeout=10 git@github.com 2>&1)"
if printf '%s' "$gh_reply" | grep -q "successfully authenticated"; then
    ok "GitHub accepts your key ($(printf '%s' "$gh_reply" | grep -o 'Hi [^!]*'))"
else
    bad "GitHub SSH login failed: $(printf '%s' "$gh_reply" | tail -n1)"
fi

echo "This repo"
case "$hub" in
    /mnt/*) note "hub is under $hub; move it to ~/learning-hub for speed (step 2)" ;;
    *)      ok "location: $hub" ;;
esac
if git -C "$hub" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    ok "is a git repo"
    remote="$(git -C "$hub" remote get-url origin 2>/dev/null)"
    [ -n "$remote" ] && ok "origin = $remote" || bad "no remote → git remote add origin git@github.com:<github-user>/learning-hub.git"
    if git -C "$hub" rev-parse --abbrev-ref '@{u}' >/dev/null 2>&1; then
        ahead="$(git -C "$hub" rev-list --count '@{u}..HEAD')"
        [ "$ahead" -eq 0 ] && ok "everything pushed" || note "$ahead commit(s) not pushed yet → git push"
    else
        note "branch not pushed yet → git push -u origin main"
    fi
    nested="$(find "$hub" -mindepth 2 -name .git 2>/dev/null)"
    [ -z "$nested" ] && ok "no nested .git folders" || bad "nested git repo(s): $nested"
else
    bad "not a git repo yet → cd $hub && git init (step 7)"
fi

echo
if [ "$fails" -eq 0 ]; then
    printf '\033[32mAll good.\033[0m\n'
else
    printf '\033[31m%d thing(s) to fix.\033[0m See notes/github-setup-wsl.md\n' "$fails"
fi
exit "$fails"
