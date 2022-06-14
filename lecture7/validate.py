import re

email = input("What's your email? ").strip()

if re.search("^\w+@\w+\.(com|edu|gov|net|dk|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
