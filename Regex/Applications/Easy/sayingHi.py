import re
import sys

#greeting pattern
Regex_Pattern = r'^[Hh][Ii][\s][^Dd]'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#for each input, print if matches greeting
while n > 0:
    Test_String = inputText.readline()
    if ( len(re.findall(Regex_Pattern, Test_String)) > 0 ):
        print Test_String,
    n = n - 1
