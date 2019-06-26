import re
import sys

inputText = sys.stdin
n = int(inputText.readline())
lines = []

while n > 0:
    lines.append(inputText.readline())
    n = n - 1

#print lines

t = int(inputText.readline())

while t > 0:
    match = []
    word = inputText.readline()
    word = word.replace("\n", "")
    #print "Word:", word
    Regex_Pattern = r'(^|(?<=[\W]))'+ re.escape(word) + '((?=[\W])|$)'
    #print "RegEx:", Regex_Pattern
    for line in lines:
        #print "re.FA:", re.findall(Regex_Pattern, line)
        match.extend(re.findall(Regex_Pattern, line))
    #print "Match:", match
    print len(match)
    t = t - 1
