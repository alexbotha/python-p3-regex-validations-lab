import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][']*([A-z][ \-']{0,1})+"
name_regex = re.compile(name)

phone_number = r"[\d+]\S+\s+\d+\S+"
phone_regex = re.compile(phone_number)

email_address = r""
email_regex = re.compile(email_address)
