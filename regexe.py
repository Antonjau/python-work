import re

email = input("what is your email address?").strip()

if re.search("@.+.com", email):
    print("valid")
else:
    print("invalid")