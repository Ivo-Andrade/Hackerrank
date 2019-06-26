import re
import sys

Regex_Pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'    # Do not delete 'r'.

inputText = sys.stdin
n = int(inputText.readline())

while n > 0:
    match = []
    Test_String = inputText.readline()
    match.extend(re.findall(Regex_Pattern, Test_String))
    if (len(match)>0):
        print "YES"
    else:
        print "NO"
    n = n - 1
