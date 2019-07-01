import re
import sys

#Java pattern
regexJava = r'import'

#C pattern
regexC = r'#include'

#from input, detect language
inputText = sys.stdin.read()
if re.search(regexJava,inputText):
    print "Java"
elif re.search(regexC,inputText):
    print "C"
else:
    print "Python"
