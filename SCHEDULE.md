# Weekly rhythm

About **4–4.5 hours a week** in four fixed slots. "Fixed" means you choose the slots once and treat them like appointments: planned ahead, not squeezed into whatever gap appears.

| Slot | Length | What happens | Suggested day |
|---|---|---|---|
| **S1 · Language** | 60 min | Learn + small exercises in the phase's main language | Tue |
| **S2 · Linux** | 60 min | One Linux topic, practised in a real terminal | Thu |
| **S3 · Build** | 90–120 min | Work on the current mini-project | Sat/Sun morning, or a weekday if weekends are taken |
| **R · Review** | 20–30 min | Close this week, set up the next | Fri or Sun |

## My slots

Fill these in during Week 1 and don't renegotiate them every week.

- S1: Python (day, time)
- S2: build tools Linux
- S3: Github init
- Review: ______

---

## How a session runs

### S1 / S2 · 60 min

1. **5 min**: reread the last session's log line and notes.
2. **35 min**: read or watch the material. Type every example yourself.
3. **15 min**: one small exercise of your own, slightly different from the example.
4. **5 min**: two or three lines in the week's log. Anything worth keeping goes into `notes/`.

### S3 · 90–120 min

1. **10 min**: pick *one* concrete goal for today ("parse the dates from the filename", not "work on the script").
2. **The rest**: build it.
3. **Last 10 min**: commit with a clear message and write the next step in the log, so next time starts fast.

### R · Review · 20–30 min

1. Fill in the minutes per session and `hours_done` in the week's frontmatter.
2. Tick topics in `progress/*.md` you could now explain to someone.
3. Three-line reflection: what clicked, what was hard, what to change.
4. Update the *Right now* box in `README.md`.
5. Create next week's note (copy `weeks/_template.md` for now, later `python new_week.py`).
6. One growth task from [progress/growth.md](progress/growth.md), 10–15 min.
7. `git add . && git commit -m "week N review" && git push`

---

## Rules that keep it steady

- **Missed a session?** Move it once within the same week. If it doesn't fit, drop it. Never double up the next week.
- **Bad week?** Do the minimum: one 30-minute session plus the review. Keeping the chain going matters more than the hours.
- **Stuck for more than 20 minutes?** Write down exactly what you tried and what happened, then ask (Claude, a forum, the docs) or park it and move on.
- **Break weeks are real breaks.** Only fill them if you want to.
- **At each phase review** (Weeks 7, 13, 19, 26), adjust the next phase instead of forcing the original plan.
- **Ahead of plan?** Don't speed up. Go deeper on the current mini-project instead.
- **Keep work out of this repo.** No client names, devices or internal tools. It's public.
