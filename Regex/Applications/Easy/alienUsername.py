import re
import sys

#alien username pattern
regex = r'^[_\.][0-9]+[a-zA-Z]*[_]{0,1}$'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#for each line, validate if alien username
while n > 0:
    match = []
    line = inputText.readline()
    line = line.replace("\n", "")
    match.extend(re.findall(regex,line))
    if len(match) == 0:
        sys.stdout.write('IN')
    print "VALID"
    n = n - 1
