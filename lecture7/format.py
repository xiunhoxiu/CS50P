import re

name = input("what is your name? ").strip()
matches = re.search("^(.+), (.+)$", name)
if matches:
    last, first = matches.group(1) + matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")