import re
import sys

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#retrive lines
lines = []
while n > 0:
    lines.append(inputText.readline())
    n = n - 1

#retrive T
inputText = sys.stdin
t = int(inputText.readline())

#for each subword, check frequency
while t > 0:
    match = []
    word = (inputText.readline())
    word = word.replace("\n", "")
    regex = re.compile('\w({})\w'.format(word))
    for line in lines:
        match.extend(re.findall(regex,line))
    print len(match)
    t = t - 1
