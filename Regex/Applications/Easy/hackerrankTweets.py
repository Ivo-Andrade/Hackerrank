import re
import sys

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#for each line, validate coords
cont = 0
while n > 0:
    line = inputText.readline()
    if re.search(r'hackerrank', line, re.IGNORECASE):
        cont = cont + 1
    n = n - 1

print cont
