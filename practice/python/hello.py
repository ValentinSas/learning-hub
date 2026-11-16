import datetime as dt

d = dt.date.today()
iso = d.isocalendar()
HUB_START = dt.date(2026, 11, 16)
hub_week = (d - HUB_START).days // 7 + 1
print(f"Today is {d.strftime('%A %d %B %Y')}")
print(f"ISO week number: {iso.week:02d}")
print(f"Hub week number: {hub_week}")
print(f"Today's week note: weeks/{iso.year}-W{iso.week:02d}.md")