import re
import sys

#phone number pattern
regex = r'^(\d*)(?: |-)(\d*)(?: |-)(\d*)'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#for each line, split phone number
while n > 0:
    line = inputText.readline()
    match = re.search(regex, line).groups()
    sys.stdout.write('CountryCode=')
    sys.stdout.write(match[0])
    sys.stdout.write(',LocalAreaCode=')
    sys.stdout.write(match[1])
    sys.stdout.write(',Number=')
    print match[2]
    n = n - 1
