import datetime as dt
from pathlib import Path
import shutil

d=dt.datetime.now().strftime('%a %d %B %Y')
print("Today is "+d)
print("ISO week number: "+str(dt.datetime.now().isocalendar()[1]))
print("Hub week number: "+str(dt.datetime.now().isocalendar()[1]))
print("Today's week note: "+str("weeks/2026-W47.md"))