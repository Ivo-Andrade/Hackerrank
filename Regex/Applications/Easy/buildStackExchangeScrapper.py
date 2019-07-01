import re
import sys

#question, time pattern
regexQuestion = r'questions/([0-9]+).*question-hyperlink\">(.*)</a></h3>'
regexTime = r'relativetime\">([^<]*)</span>'

#from input, check for questions
questions =[]
time = []
inputText = sys.stdin.read()
questions.extend(re.findall(regexQuestion, inputText))
time.extend(re.findall(regexTime, inputText))

#print questions
pos = 0
for question in questions:
    sys.stdout.write(question[0]+";")
    sys.stdout.write(question[1]+";")
    print time[pos]
    pos = pos + 1
