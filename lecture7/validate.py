import re

email = input("What's your email? ").strip()

if re.search("^\w+@\w+\.(com|edu|gov|net|dk|org)$", email):
    print("Valid")
else:
    print("Invalid")
