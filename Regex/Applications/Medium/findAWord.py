import re
import sys

#retrive N
inputText = sys.stdin
n = int(inputText.readline())
lines = []

#retrive lines
while n > 0:
    lines.append(inputText.readline())
    n = n - 1

#retrive T
t = int(inputText.readline())

#for each word, find match frequency in lines
while t > 0:
    match = []
    word = inputText.readline()
    word = word.replace("\n", "")
    Regex_Pattern = r'(^|(?<=[\W]))'+ re.escape(word) + '((?=[\W])|$)'
    for line in lines:
        match.extend(re.findall(Regex_Pattern, line))
    print len(match)
    t = t - 1
