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

#for each word
while t > 0:
    match = []
    word = inputText.readline()         #retrive word
    word = word.replace("\n", "")               #remove \n char
    Regex_Pattern = r'(^|(?<=[\W]))'+ re.escape(word) + '((?=[\W])|$)'              #update regEx
    for line in lines:
        match.extend(re.findall(Regex_Pattern, line))       #for each line, find matches
    print len(match)            #print match frequency
    t = t - 1
