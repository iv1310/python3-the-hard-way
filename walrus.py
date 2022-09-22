import re

test = "Something to match"

pattern1 = r"^.*(thing).*"
pattern2 = r"^.*(not present).*"

m = re.match(pattern1, test)
if m:
    print(f"Matched the 1st pattern: {m.group(1)}")
else:
    m = re.match(pattern2, test)
    if m:
        print(f"Matched the 2nd pattern: {m.group(1)}")

# ---------------------
# Cleaner
if m := (re.match(pattern1, test)):
    print(f"Matched the 1st pattern: {m.group(1)}")
elif m := (re.match(pattern2, test)):
    print(f"Matched the 2nd pattern: {m.group(1)}")
