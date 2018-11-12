# Brandon Campbell
# Fall 2018 CS 355
# Assignment 4 part 2

import assignment4Part1
import re


def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

# The it argument is an iterator. The sequence of return characters should
# represent a string of properly nested {} parentheses pairs, from which
# the leasing '{' has been removed. If the parentheses are not properly
# nested, returns False.


def groupMatching(it):
    res = []
    for c in it:
        if c == '}':
            return res
        else:
            # Note how we use a recursive call to group the inner matching
            # parenthesis string and append it as a whole to the list we are
            # constructing. Also note how we have already seen the leading
            # '{' of this inner group and consumed it from the iterator.
            res.append(groupMatching(it))
    return False

# Function to parse a string of { and } braces. Properly nested parentheses
# are arranged into a list of properly nested lists.


def group(s):
    res = []
    it = iter(s)
    for c in it:
        if c == '}':  # non matching closing paranthesis; return false
            return False
        else:
            res.append(groupMatching(it))
    return res

# group("{{}{{}}}")


# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parentheses in the input iterator is not properly nested, returns False.
def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c == '{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code array for the inner
            # parentheses, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatching2(it))
        else:
            res.append(c)
    return False


# RENAME THIS FUNCTION AS parse
# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c == '}':  # non matching closing paranthesis; return false since there is
                    # a syntax error in the Postscript code.
            return False
        elif c == '{':
            res.append(groupMatching2(it))
        else:
            if isInt(c):
                res.append(int(c))
            elif isFloat(c):
                res.append(float(c))
            elif isTrue(c):
                res.append(True)
            elif isFalse(c):
                res.append(False)
            else:
                res.append(c)
    return res


def alterArray(value):
    for i in range(0, (len(value) - 1)):
        if isArray(value[i]):
            value[i] = convertToArray(value[i])
        else:
            continue


def isArray(value):
    for i in range(1, (len(value) - 2), 2):
        if isInt(value[i]):
            continue
        else:
            return False

    return True


def convertToArray(value):
    return_array = []
    for item in value:
        if item == '[' or item == ']' or item == ' ':
            continue
        else:
            return_array.append(item)

    return return_array


def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def isTrue(value):
    if value == 'True':
        return True


def isFalse(value):
    if value == 'False':
        return False


# Write the necessary code here; again write
# auxiliary functions if you need them. This will probably be the largest
# function of the whole project, but it will have a very regular and obvious
# structure if you've followed the plan of the assignment.
#
def interpretSPS(code): # code is a code array
    pass


# Copy this to your HW4_part2.py file>
def interpreter(s): # s is a string
    # interpretSPS(parse(tokenize(s)))
    pass


# testing

input1 = """
  /square {dup mul} def  
  [1 2 3 4] {square} forall 
  add add add 30 eq true 
  stack
"""


input2 = """ 
  [1 2 3 4 5] dup length /n exch def
  /fact {
      0 dict begin
         /n exch def
         n 2 lt
         { 1}
         {n 1 sub fact n mul }
         ifelse
      end 
  } def
  n fact stack    
"""


input3 = """
  [9 9 8 4 10] {dup 5 lt {pop} if}  forall 
  stack 
"""

input4 = """
  [1 2 3 4 5] dup length exch {dup mul}  forall
  add add add add
  exch 0 exch -1 1 {dup mul add} for
  eq stack 
"""


if __name__ == '__main__':
    variable = parse(tokenize(input3))
    print(variable)
    alterArray(variable)
    print(variable)

