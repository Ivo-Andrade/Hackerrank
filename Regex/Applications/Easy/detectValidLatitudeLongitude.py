import re
import sys

#coord pattern
regex = r'\(((\+?)|(-?))(([0-8]?[0-9])(\.[0-9]+)?|90(\.0+)?),(\s)*((\+?)|(-?))(1[0-7][0-9](\.[0-9]+)?|[0-9]?[0-9](\.[0-9]+)?|180(\.0+)?)\)'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#for each line, validate coords
while n > 0:
    line = inputText.readline()
    if re.match(regex,line):
        print "Valid"
    else:
        print "Invalid"
    n = n - 1
