import re
import sys

Regex_Pattern = r'^[Hh][Ii][\s][^Dd]'

inputText = sys.stdin
n = int(inputText.readline())

while n > 0:
    Test_String = inputText.readline()
    if ( len(re.findall(Regex_Pattern, Test_String)) > 0 ):
        print Test_String,
    n = n - 1
