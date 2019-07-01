import re
import sys

#opening tag pattern
Regex_Pattern = r'<\s*([^\/][a-zA-Z0-9]*)'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())
lines = []

#retrive lines
while n > 0:
    lines.append(inputText.readline())
    n = n - 1

#for each line, verify matches for tags
match = []
for line in lines:
    match.extend(re.findall(Regex_Pattern, line))
    
#remove duplicates, sort list
match = list(dict.fromkeys(match))
match.sort()

#print tags
for tag in match[:-1]:
    sys.stdout.write(tag + ";")

for tag in match[-1:]:
    sys.stdout.write(tag)
