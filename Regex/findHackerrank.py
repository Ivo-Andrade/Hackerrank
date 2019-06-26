import re
import sys

Regex_Pattern_StartsWith = r'^hackerrank'
Regex_Pattern_EndsWith = r'hackerrank$'

inputText = sys.stdin
n = int(inputText.readline())

while n > 0:
    Test_String = inputText.readline()
    if ( (len(re.findall(Regex_Pattern_StartsWith, Test_String)) > 0) & (len(re.findall(Regex_Pattern_EndsWith, Test_String)) > 0) ):
        print "0"
    elif ( len(re.findall(Regex_Pattern_StartsWith, Test_String)) > 0 ):
        print "1"
    elif ( len(re.findall(Regex_Pattern_EndsWith, Test_String)) > 0 ):
        print "2"
    else:
        print "-1"
    n = n - 1
