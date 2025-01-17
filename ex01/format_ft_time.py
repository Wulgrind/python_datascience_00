from time import time, strftime, localtime

seconds_since = time()

formatted_seconds = f"{seconds_since:,.4f}" 
scientific_notation = f"{seconds_since:.2e}"

now = strftime("%b %d %Y", localtime(seconds_since))

print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation")
print(now)
