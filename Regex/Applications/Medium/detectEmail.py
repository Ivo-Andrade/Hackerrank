Regex_Pattern = r'[\w+\.]*[\w]@[\w+\.]*[\w]'    # Do not delete 'r'.

import re
import sys

match = []

for Test_String in sys.stdin:
    match.extend(re.findall(Regex_Pattern, Test_String))

match = list(dict.fromkeys(match))
match.sort()

for email in match[:-1]:
    sys.stdout.write(email + ";")

for email in match[-1:]:
    sys.stdout.write(email)
