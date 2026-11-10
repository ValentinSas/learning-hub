# Roadmap · 16 Nov 2026 → 13 Jun 2027

26 learning weeks plus 4 break weeks. Roughly 4–4.5 h a week:

- **S1 · Language** (60 min)
- **S2 · Linux** (60 min)
- **S3 · Build** (90–120 min)
- **R · Review** (20–30 min)

Slot details are in [SCHEDULE.md](SCHEDULE.md). Links for every resource named here are in [RESOURCES.md](RESOURCES.md).

How to read the tables:
- **Tutorial §N** means the official Python tutorial, chapter N.
- **TLCL** is *The Linux Command Line* by William Shotts (free PDF).
- **learncpp** is learncpp.com. Chapters are named by topic in case the numbering shifts.
- **MS** is MIT's *Missing Semester* (2026 edition).

The plan is a guide, not a contract. At each phase review, move things around if something took longer or turned out easier.

---

## Phase 0 · Setup (Week 1)

**Goal:** working tools and the habit started.

| Wk | Dates | S1 · Language | S2 · Linux | S3 · Build |
|---|---|---|---|---|
| 1 | 16–22 Nov | Python: venv on Ubuntu 24.04, `hello.py`, bring your existing refresh files into `practice/`. Tutorial §1–2 | WSL2 basics: update packages, install build tools, Linux vs. `/mnt/c` files. MS lecture 1: *Introduction to the Shell* | GitHub: follow [notes/github-setup-wsl.md](notes/github-setup-wsl.md) (SSH key, first push), VS Code + WSL. Fix your slots in SCHEDULE.md |

**Done when:** the hub is on GitHub and you've done your first weekly review.

---

## Phase 1 · Python & Linux foundations (Weeks 2–7)

**Goal:** write small useful Python scripts and move around Linux without thinking about it.

| Wk | Dates | S1 · Python | S2 · Linux | S3 · Build |
|---|---|---|---|---|
| 2 | 23–29 Nov | Numbers, strings, f-strings, lists intro. Tutorial §3 | Navigation & files: `ls cd cp mv rm mkdir`, paths, `man`. TLCL ch. 1–5 | OverTheWire Bandit levels 0–5 + 2 Exercism Python exercises |
| 3 | 30 Nov–6 Dec | `if`, `for`, `while`, `range`, `break`. Tutorial §4 (up to *Defining Functions*) | Permissions, users, groups, `chmod`, `sudo`. TLCL ch. 9 | **Mini-project 1: `new_week.py`** — copies `weeks/_template.md`, fills in week number + dates |
| 4 | 7–13 Dec | Lists, tuples, dicts, sets, comprehensions. Tutorial §5 | Pipes & redirection, `grep`, `find`, `sort`, `uniq`, `wc`. TLCL ch. 6, 17 | Finish `new_week.py`, then use it to create Week 5's note |
| 5 | 14–20 Dec | Functions, arguments, defaults; modules & imports. Tutorial §4 (rest) + §6 | Processes: `ps`, `top`/`htop`, `kill`, jobs, signals. TLCL ch. 10 | **Mini-project 2: `hours.py`** — reads every week note, sums `hours_done` |
| — | 21 Dec–3 Jan | **Holiday break.** Nothing planned. Bandit levels if you feel like it. | | |
| 6 | 4–10 Jan | Reading/writing files, `pathlib`, exceptions. Tutorial §7–8 | `apt`, environment variables, `PATH`, `.bashrc`. TLCL ch. 11, 14 | Finish `hours.py`: table per week + total + average |
| 7 | 11–17 Jan | Standard library tour: `argparse`, `json`, `datetime`. Tutorial §10 | Bash scripting: variables, `if`, loops, arguments. TLCL ch. 24, 27, 29, 32–33 | `backup.sh`: add + commit + push the hub in one command. **Phase 1 review** |

**Done when:** `new_week.py`, `hours.py` and `backup.sh` work and are pushed; you can explain `chmod 755` and read a pipe chain like `grep … | sort | uniq -c` without looking it up.

---

## Phase 2 · C++ foundations & build tools (Weeks 8–13)

**Goal:** write, build and debug small multi-file C++ programs the way real projects do (CMake, gdb).

| Wk | Dates | S1 · C++ | S2 · Linux / tooling | S3 · Build |
|---|---|---|---|---|
| 8 | 18–24 Jan | learncpp: *Introduction/Getting Started* + *C++ Basics* | `g++` by hand: compile vs. link, `-Wall -Wextra -std=c++20` | 3 Exercism C++ exercises |
| 9 | 25–31 Jan | learncpp: *Functions and Files* (headers, multiple files), *Fundamental Data Types*, *Constants and Strings* | `make` and a simple Makefile | Port one of your Python exercises to C++ |
| 10 | 1–7 Feb | learncpp: *Control Flow*; *References and Pointers* | CMake: `CMakeLists.txt`, out-of-source builds. CMake tutorial steps 1–2 | **Mini-project 3: `pose2d`** — Point/Pose types, rotate + translate a point |
| 11 | 8–14 Feb | learncpp: *Enums and Structs*; *Introduction to Classes* | `gdb`: breakpoints, step, print, backtrace. MS: *Debugging and Profiling* | `pose2d`: read waypoints from a text file, compute path length |
| 12 | 15–21 Feb | learncpp: `std::vector`, `std::array`, *Iterators and Algorithms* | `ssh`, keys, `scp`, `~/.ssh/config` | `pose2d`: refactor with `std::vector` + `<algorithm>`, CMake build |
| 13 | 22–28 Feb | learncpp: *Dynamic Allocation*; *Move Semantics and Smart Pointers* (`unique_ptr` first) | git deeper: branches, merge, rebase basics. Pro Git ch. 3 / MS: *Version Control and Git* | `pose2d`: README, push as its own repo. **Phase 2 review** |
| — | 1–7 Mar | **Buffer week.** Catch up or rest. | | |

**Done when:** `pose2d` builds from a clean clone with `cmake -B build && cmake --build build`, you've found at least one bug with gdb, and you can explain reference vs. pointer.

---

## Phase 3 · Python intermediate & Linux systems → your own dashboard (Weeks 14–19)

**Goal:** replace this README with a small web dashboard you wrote, running as a Linux service. This is the "own app later" part.

| Wk | Dates | S1 · Python | S2 · Linux | S3 · Build: Hub dashboard |
|---|---|---|---|---|
| 14 | 8–14 Mar | Classes, `dataclasses`. Tutorial §9 | systemd: `systemctl`, unit files, user services | Parser v1: read each week note's frontmatter into a `Week` dataclass (parse it by hand) |
| 15 | 15–21 Mar | Type hints, PEP 8, `ruff` | Logs: `journalctl`, `/var/log` | Parser: also count `[x]` / `[ ]` in `progress/*.md` |
| 16 | 22–28 Mar | Testing with `pytest` | Networking: `ip`, `ping`, `ss`, ports, DNS. TLCL ch. 16 | Tests for the parser |
| 17 | 29 Mar–4 Apr | Regex (`re`), YAML with PyYAML | cron vs. systemd timers | Swap the hand parser for PyYAML (tests should still pass). FastAPI app, first page: current week + hours |
| 18 | 5–11 Apr | Jinja2 templates, minimal HTML/CSS | `ufw` firewall, ssh tunnels, Tailscale | Dashboard: progress bars per track, links to RESOURCES |
| 19 | 12–18 Apr | `logging`, config files, `pyproject.toml` | `tmux`, aliases, dotfiles in git. MS: *Command-line Environment* | Run the dashboard as a systemd user service; README + screenshot. **Phase 3 review** |

**Done when:** `systemctl --user status hub` shows it running, it reads this repo's files live, and the parser has tests.

---

## Phase 4 · ROS 2: where the three tracks meet (Weeks 20–26)

**Goal:** one small ROS 2 package with a C++ node and a Python node working together.
You're on Ubuntu 24.04 (WSL2), so use **ROS 2 Jazzy Jalisco** (LTS, supported until 2029). GUI tools like turtlesim and RViz2 open as normal windows through WSLg. (If you ever move to Ubuntu 26.04, the matching LTS is Lyrical Luth; the tutorials are nearly identical.)

| Wk | Dates | S1 · ROS 2 concepts | S2 · Linux / tooling | S3 · Build |
|---|---|---|---|---|
| 20 | 19–25 Apr | Nodes, topics, messages | Install ROS 2 Jazzy (deb packages), source the setup file, `ros2` CLI, turtlesim | ROS docs: *Beginner: CLI tools* tutorials |
| — | 26 Apr–2 May | **Easter + 1 May break.** Optional: finish the CLI tutorials. | | |
| 21 | 3–9 May | `rclpy`: publisher & subscriber | Workspaces, `colcon build`, `rosdep` | Tutorial: *Writing a simple publisher and subscriber (Python)* |
| 22 | 10–16 May | `rclcpp`: same in C++ | `ament_cmake`, `package.xml`, CMake inside ROS | Tutorial: *Writing a simple publisher and subscriber (C++)* |
| 23 | 17–23 May | Services and parameters (Python + C++) | Introspection: `ros2 topic/service/param`, `rqt` | **Mini-project 4: `turtle_patrol`** — C++ node drives turtlesim through waypoints (reuse `pose2d`) |
| 24 | 24–30 May | Launch files (Python launch), tf2 intro | `ros2 bag record` / `play` | `turtle_patrol`: Python node tracks distance travelled and logs it |
| 25 | 31 May–6 Jun | RViz2 basics | Revisit systemd: start a ROS launch file at boot | `turtle_patrol`: one launch file starts everything; record a bag |
| 26 | 7–13 Jun | Reread your notes, fill the gaps | Tidy your Linux cheat sheets | README + demo GIF. **6-month retrospective** (see below) |

**Done when:** `ros2 launch turtle_patrol patrol.launch.py` works from a clean clone and you can explain topics vs. services vs. parameters.

---

## After Week 26: choose a branch

Write the retrospective in [progress/growth.md](progress/growth.md), look at the postings you collected, then pick one:

**Research track** (humanoid, soft robotics, exoskeletons)
- Linear algebra + control refresher (state space, PID → LQR)
- Simulation: MuJoCo or Gazebo
- Eigen in C++, numpy/scipy in Python
- Reproduce one small result from a paper (e.g. inverted pendulum, simple leg model)

**Industry track** (autonomous mobile robots, robot arms)
- Nav2 with a simulated mobile robot
- MoveIt 2 with a simulated arm
- Industrial comms: OPC UA, Modbus TCP
- Docker for deploying robot software
