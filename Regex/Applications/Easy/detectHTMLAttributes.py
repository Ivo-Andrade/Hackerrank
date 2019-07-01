import re
import sys

def takeFirst(elem):
    return elem[0]

#opening tag <tag, atributes> pattern
regexTag = r'<\s*([^\/][a-zA-Z0-9]*)\s*([^>]*)>'

#attributes pattern
regexAttribute = r'([a-zA-Z0-9]*)=(?:"|\')'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())
lines = []

#retrive lines
while n > 0:
    lines.append(inputText.readline())
    n = n - 1

#for each line, verify matches for tags
matches = []
for line in lines:
    matches.extend(re.findall(regexTag, line))
matches.sort(key=takeFirst)

#creates tag dictionary
tags = {}
for match in matches:
    tag, attributes = match
    if tag not in tags:
        tags[tag] = re.findall(regexAttribute,attributes)
    else:
        tags[tag].extend(re.findall(regexAttribute,attributes))

#ordering dictionary
for tag in tags:
    tags[tag] = list(dict.fromkeys(tags[tag]))
    tags[tag].sort()

#print
for tag in sorted(tags.keys()):
    sys.stdout.write('%s:'%tag)
    attrs = tags.get(tag)
    for attr in attrs[:-1]:
        sys.stdout.write('%s,'%attr)
    for attr in attrs[-1:]:
        sys.stdout.write('%s'%attr)
    sys.stdout.write('\n')
