#Email pattern
Regex_Pattern = r'[\w+\.]*[\w]@[\w+\.]*[\w]'    # Do not delete 'r'.

import re
import sys

match = []

#from input, find Email matches
for Test_String in sys.stdin:
    match.extend(re.findall(Regex_Pattern, Test_String))

#remove duplicates, sort list
match = list(dict.fromkeys(match))
match.sort()

#print Emails
for email in match[:-1]:
    sys.stdout.write(email + ";")

for email in match[-1:]:
    sys.stdout.write(email)
