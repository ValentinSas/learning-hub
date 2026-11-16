import datetime as dt
from pathlib import Path
import shutil

d=dt.datetime.today()
iso=d.isocalendar()
print("Today is "+d.strftime('%A %d %B %Y'))
print("ISO week number: "+str(iso[1]))
print("Hub week number: "+str(iso[2]))
print("Today's week note: "+str("weeks/2026-W47.md"))