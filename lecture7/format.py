import re

name = input("what is your name? ").strip()
matches = re.search("^.+, .+$", name)
