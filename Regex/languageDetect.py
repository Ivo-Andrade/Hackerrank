Regex_Pattern = r'[A-Z]+'    # Do not delete 'r'.

import re
import sys

strLangs = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC"
languages = []
languages.extend(re.findall(Regex_Pattern, strLangs))

inputText = sys.stdin
n = int(inputText.readline())

while n > 0:
    match = []
    Test_String = inputText.readline()
    match.extend(re.findall(Regex_Pattern, Test_String))
    if (any(item in languages for item in match)):
        print "VALID"
    else:
        print "INVALID"
    n = n - 1
