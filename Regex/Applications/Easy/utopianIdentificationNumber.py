import re
import sys

#utopian number pattern
regex = r'[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#for each line, validate if utopian number
while n > 0:
    line = inputText.readline()
    line = line.replace("\n", "")
    if not re.match(regex,line):
        sys.stdout.write("IN")
    print "VALID"
    n = n - 1
