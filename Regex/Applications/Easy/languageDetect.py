#word pattern
Regex_Pattern = r'[A-Z]+'

import re
import sys

#supported languages list
strLangs = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC"
languages = []
languages.extend(re.findall(Regex_Pattern, strLangs))

#retrive N
inputText = sys.stdin
n = int(inputText.readline())

#for each input, validate if language is supported
while n > 0:
    match = []
    Test_String = inputText.readline()
    match.extend(re.findall(Regex_Pattern, Test_String))
    if (any(item in languages for item in match)):
        print "VALID"
    else:
        print "INVALID"
    n = n - 1
