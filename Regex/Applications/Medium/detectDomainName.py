import re
import sys

#domain pattern
regex = r'(?:https*:\/\/(?:www\.|ww2\.)*)((?:[a-zA-Z0-9\-]*\.)+(?:[a-zA-Z0-9\-]*))'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#retrive lines
lines = []
while n > 0:
    lines.append(inputText.readline())
    n = n - 1

#for each line, find links
links = []
for line in lines:
    links.extend(re.findall(regex, line))

#remove duplicates, sort list
links = list(dict.fromkeys(links))
links.sort()

#print domains
for link in links[:-1]:
    sys.stdout.write(link)
    sys.stdout.write(";")

for link in links[-1:]:
    sys.stdout.write(link)
