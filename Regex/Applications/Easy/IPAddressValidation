import re
import sys

#IPv4 pattern
regexIPv4 = r'^(([0-9]{1,2}|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'

#IPv6 pattern
regexIPv6 = r'^(([0-9a-f]{1,4}):){7}([0-9a-f]{1,4})$'

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#for each line, validate if IPv4, IPv6or neither
while n > 0:
    line = inputText.readline()
    line = line.replace("\n", "")
    if re.match(regexIPv4,line):
        print "IPv4"
    elif re.match(regexIPv6,line):
        print "IPv6"
    else:
        print "Neither"
    n = n - 1
