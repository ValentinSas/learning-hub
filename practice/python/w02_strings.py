"""
Week 2 · Python strings

Replace every `...` with an expression, then run:

    python w02_strings.py

Each check prints ✓ or ✗ with what you got vs. what was expected.
Work top to bottom; one expression per answer, no hard-coded results
(write note[6:10], not "2026"). Reference: Python Tutorial §3.1.2 (Text).
"""


def check(label, got, expected):
    if got == expected:
        print(f"  ✓ {label}")
    else:
        print(f"  ✗ {label}: got {got!r}, expected {expected!r}")


# ---------------------------------------------------------------------------
print("1 · Indexing and slicing")
note = "weeks/2026-W48.md"
#       01234567890123456   ← positions, to help you count

first_char = note[0]    # the first character
last_char = note[-1]     # the last character, using a negative index
year = note[6:10]          # "2026", with a slice
week = int(note[12:14])          # 48 as an int (slice, then convert)
stem = note[6:14]          # "2026-W48": no folder, no ".md"
backwards = note[::-1]     # the whole string reversed, with one slice

check("first_char", first_char, "w")
check("last_char", last_char, "d")
check("year", year, "2026")
check("week", week, 48)
check("stem", stem, "2026-W48")
check("backwards", backwards, "dm.84W-6202/skeew")


# ---------------------------------------------------------------------------
print("2 · String methods")
raw = "   Learning Hub: Python, C++, Linux   "
parts = ["Python", "C++", "Linux"]

clean = raw.strip(" ")         # raw without the spaces at both ends
shout = clean.upper()         # clean, in capitals (you can chain: raw.a().b())
tracks = clean.split(": ")[1].split(", ")        # ["Python", "C++", "Linux"], built from raw with split
joined = ' | '.join(parts)        # "Python | C++ | Linux", built from parts
n_count = clean.split(": ")[0].lower().count("n")       # how many times "n" appears in "Learning Hub" (case-insensitive)
is_week = note.startswith("weeks/")       # True if note starts with "weeks/"
next_note = note.replace("W48", "W49")     # note, with "W48" swapped for "W49"

check("clean", clean, "Learning Hub: Python, C++, Linux")
check("shout", shout, "LEARNING HUB: PYTHON, C++, LINUX")
check("tracks", tracks, ["Python", "C++", "Linux"])
check("joined", joined, "Python | C++ | Linux")
check("n_count", n_count, 2)
check("is_week", is_week, True)
check("next_note", next_note, "weeks/2026-W49.md")


# ---------------------------------------------------------------------------
print("3 · Pulling data out of a log line")
line = "2026-11-25 08:43:12 WARN robot_03 battery=18% speed=0.8"
# Hint: line.split() gives you a list of the space-separated pieces.

time_only = line.split()[1]     # "08:43:12"
level = line.split()[2]         # "WARN"
robot = line.split()[3]         # "robot_03"
# list(enumerate(line.split()))
# [(0, '2026-11-25'), (1, '08:43:12'), (2, 'WARN'), (3, 'robot_03'), (4, 'battery=18%'), (5, 'speed=0.8')]
# print(list(enumerate(line.split())))
battery = int(line.split()[4].split("=")[1].rstrip("%"))       # 18 as an int (get rid of "battery=" and "%")
speed = float(line.split()[5].split("=")[1])         # 0.8 as a float

check("time_only", time_only, "08:43:12")
check("level", level, "WARN")
check("robot", robot, "robot_03")
check("battery", battery, 18)
check("speed", speed, 0.8)


# ---------------------------------------------------------------------------
print("4 · f-strings")
name = "Vali"
hours = 4.5
week_no = 2
progress = 0.3333

studied = f"{name} studied {hours} h in week {week_no}"       # "Vali studied 4.5 h in week 2"
pct = f"Progress: {progress:.1%}"           # "Progress: 33.3%"   (look up the % format spec)
tag = f"W{week_no:02d}"           # "W02"               (pad week_no to 2 digits)
row = f"{'Python':<10}|{hours:>5}"  # "Python    |  4.5"  ("Python" left-aligned in 10, hours right-aligned in 5)
debug = f"{hours=}"         # "hours=4.5"         (there's a one-character f-string trick for this)

check("studied", studied, "Vali studied 4.5 h in week 2")
check("pct", pct, "Progress: 33.3%")
check("tag", tag, "W02")
check("row", row, "Python    |  4.5")
check("debug", debug, "hours=4.5")


# ---------------------------------------------------------------------------
 #5 · Not checked here: try these in the REPL and write what happens in your log.
s="hub"
#s[0] = "H"        # why does this fail?
#s is a string, is imutable, so you can't change its characters in place. You can only make a new string from it.
s = "H" + s[1:]   # and why does this work?
#this is a new string, made by concatenating "H" with the rest of s (s[1:]), which is "ub", so it becomes "Hub".
print("Muie")