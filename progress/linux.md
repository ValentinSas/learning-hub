# Linux

**Status:** Not started
**Now working on:** —
**Last updated:** 2026-11-10
**My setup:** WSL2 · Ubuntu 24.04 LTS (repo lives in `~/learning-hub`, not on `/mnt/c`)

Tick a topic when you can do it without looking it up (or know exactly where to look).

## Phase 0–1 · Shell foundations

- [ ] Navigation: `pwd`, `ls`, `cd`, absolute vs. relative paths
- [ ] Files: `cp`, `mv`, `rm`, `mkdir`, `touch`, wildcards
- [ ] Getting help: `man`, `--help`, `apropos`
- [ ] Permissions: `rwx`, `chmod` (numeric + symbolic), `chown`, `sudo`
- [ ] Pipes and redirection: `|`, `>`, `>>`, `2>`
- [ ] Text tools: `grep`, `sort`, `uniq`, `wc`, `head`, `tail`
- [ ] Finding things: `find`, `locate`
- [ ] Processes: `ps`, `top`/`htop`, `kill`, `jobs`, `fg`/`bg`, signals
- [ ] Packages: `apt update/install/remove`
- [ ] Environment: variables, `PATH`, `.bashrc`
- [ ] Bash scripts: shebang, variables, `if`, loops, `$1 $@`

## Phase 2 · Dev tooling

- [ ] `ssh`, key pairs, `scp`, `~/.ssh/config`
- [ ] git: branches, merge, rebase basics

## Phase 3 · Systems

- [ ] systemd: `systemctl`, writing a unit file, user services
- [ ] Logs: `journalctl -u … -f`
- [ ] Networking: `ip a`, `ping`, `ss -tulpn`, ports, DNS
- [ ] Scheduling: cron, systemd timers
- [ ] Firewall (`ufw`), ssh tunnels, Tailscale
- [ ] `tmux`, aliases, dotfiles in git

## Phase 4 · ROS 2 on Linux

- [ ] Installing ROS 2, sourcing setup files
- [ ] `colcon build`, workspaces, `rosdep`
- [ ] `ros2 bag`
- [ ] Starting a launch file at boot with systemd

## Built with it

| Project | What it does | Where |
|---|---|---|
| `backup.sh` | Commits and pushes the hub in one command | `practice/bash/` |
| Hub service | Dashboard running as a systemd user service | — |

## Gotchas I hit

-
