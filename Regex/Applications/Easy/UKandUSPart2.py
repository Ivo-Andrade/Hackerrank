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
t = int(inputText.readline())

#for each t case, verify US/UK word variant matches
while t > 0:
    word = inputText.readline()
    word = word.replace("\n", "")
    regex = r'(?:(?<=\s)|(?<=^))' + re.escape(word) + r'(?:(?=\s)|(?=$))'
    listMatches = []
    for line in lines:
        line = re.sub('ou?r', 'our', line)
        listMatches.extend(re.findall(regex, line))
    print len(listMatches)
    t = t - 1
