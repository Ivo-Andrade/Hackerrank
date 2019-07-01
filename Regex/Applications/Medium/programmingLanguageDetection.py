import re
import sys

#Non-Python pattern
regexNotPython = r';$'

#C pattern
regexC = r'#include'

#from input, detect language
inputText = sys.stdin.read()
if re.search(regexNotPython,inputText):
    if re.search(regexC,inputText):
        print "C"
    else:
        print "Java"
else:
    print "Python"
