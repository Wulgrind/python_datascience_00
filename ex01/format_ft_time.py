from time import time, strftime, localtime
from datetime import datetime

seconds_since = time()

scientific_notation = f"{seconds_since:.2e}"

now = strftime("%b %d %Y", localtime(seconds_since))

print(f"Seconds since January 1, 1970: {seconds_since} or {scientific_notation}$")
print(now)