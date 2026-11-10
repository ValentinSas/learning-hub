# Learning Hub

My own plan for getting solid at **Python, C++ and Linux**, then bringing them together in **ROS 2**.
About 4 hours a week, in fixed slots I plan in advance. It doesn't depend on any employer, and everything I build ends up here or on GitHub.

---

## Right now

> Update this box during every weekly review.

| | |
|---|---|
| **Phase** | 0 · Setup |
| **This week** | [Week 1 · 16–22 Nov 2026](weeks/2026-W47.md) |
| **Next milestone** | Hub pushed to GitHub ([setup guide](notes/github-setup-wsl.md)), session slots fixed |
| **Setup** | WSL2 · Ubuntu 24.04 · VS Code |
| **Hours so far** | 0 |
| **Last review** | — |

## Tracks

| Track | Status | Progress |
|---|---|---|
| Python | Not started | [progress/python.md](progress/python.md) |
| C++ | Not started | [progress/cpp.md](progress/cpp.md) |
| Linux | Not started | [progress/linux.md](progress/linux.md) |
| Growth (CV, network, reading) | Not started | [progress/growth.md](progress/growth.md) |

## The plan at a glance

| Phase | Weeks | Dates | Main focus | Mini-project |
|---|---|---|---|---|
| 0 · Setup | 1 | 16–22 Nov 2026 | Tools, git, first script | This hub on GitHub |
| 1 · Foundations | 2–7 | 23 Nov 2026 – 17 Jan 2027 | Python + Linux basics | `new_week.py`, `hours.py`, `backup.sh` |
| 2 · C++ | 8–13 | 18 Jan – 28 Feb 2027 | C++ + build tools, gdb, ssh | `pose2d` (2D poses, path length) |
| 3 · Systems | 14–19 | 8 Mar – 18 Apr 2027 | Python intermediate + Linux services | **Hub dashboard** (replaces this README) |
| 4 · ROS 2 | 20–26 | 19 Apr – 13 Jun 2027 | rclpy + rclcpp, colcon, launch | `turtle_patrol` |

Breaks: 21 Dec – 3 Jan (holidays), 1–7 Mar (buffer), 26 Apr – 2 May (Easter + 1 May).
Full week-by-week plan: **[ROADMAP.md](ROADMAP.md)**

## How this works

1. **[ROADMAP.md](ROADMAP.md)** says what each week is about.
2. Each week gets its own note in [`weeks/`](weeks/), made from [`weeks/_template.md`](weeks/_template.md) (by hand for now, later with the `new_week.py` script you write in Weeks 3–4).
3. Every week has four slots: **S1** language, **S2** Linux, **S3** build, **R** review. See **[SCHEDULE.md](SCHEDULE.md)**.
4. During the review: tick topics in [`progress/`](progress/), log your hours, update the *Right now* box above.
5. Commit and push. Your git history is your progress log.

```bash
git add .
git commit -m "week 1 review"
git push
```

## Folder map

```
learning-hub/
├── README.md          ← you are here (home page)
├── ROADMAP.md         ← week-by-week plan
├── SCHEDULE.md        ← weekly rhythm + rules
├── RESOURCES.md       ← documentation library
├── progress/          ← one checklist per track
├── weeks/             ← one note per week (+ template)
├── notes/             ← cheat sheets, things worth keeping
├── practice/          ← exercises (python/, cpp/, bash/)
└── projects/          ← index of the mini-projects
```

## Ground rules

- Steady beats intense. A short week still counts. A skipped review doesn't.
- Type the examples yourself, don't copy-paste.
- **Nothing from work goes in here** (clients, devices, internal tools). This repo is public.
- Opens fine in [Obsidian](https://obsidian.md/) (open the folder as a vault), in VS Code, or straight on GitHub.
