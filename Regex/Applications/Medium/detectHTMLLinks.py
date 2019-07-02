import re
import sys

#link, text pattern
regex = r'<a href="([^"]*)"[^>]*>(?:<[^a>]*>)*([^<]*)(?:<[^>]*>)*<\/a>'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#for each line, check for a tags
links = []
while n > 0:
    line =  inputText.readline()
    links.extend(re.findall(regex, line))
    n = n - 1

#for each link, print
for link in links:
    sys.stdout.write(link[0].lstrip()+",")
    print link[1].lstrip()
