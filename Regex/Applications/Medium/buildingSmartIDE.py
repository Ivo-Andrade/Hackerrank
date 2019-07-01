import re
import sys

#comment pattern
regex = r'(\/\/.*|\/\*[^\*]*\*\/|\/\*\*[^\*]*\*\*\/)'

#from input, check for comments
comments =[]
inputText = sys.stdin.read()
comments.extend(re.findall(regex, inputText))

#print comments
for comment in comments:
    print re.sub(r'(^[ \t]+|[ \t]+(?=:))', '', comment, flags=re.M)
