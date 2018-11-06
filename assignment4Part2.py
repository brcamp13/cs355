# Brandon Campbell
# Fall 2018 CS 355
# Assignment 4 part 2

import assignment4Part1
import re


def tokenize(s):
 return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

 # Do all of the parsing stuff (She gives the necessary code for parsing)
 
 def interpretSPS(code): 
     pass

def interpreter(s):
    pass


if __name__ == '__main__':
    interpreter()