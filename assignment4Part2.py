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


def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c == '{':
            res.append(groupMatching2(it))
        else:
            res.append(c)
    return False


# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c == '}':  # non matching closing parenthesis; return false since there is
                    # a syntax error in the Postscript code.
            return False
        elif c == '{':
            res.append(groupMatching2(it))
        else:
            res.append(c)
    return res







#~~~~~~~~~~~~~~~~~~~~~~~~~NOTES FOR MYSELF, FEEL FREE TO IGNORE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Okay, so the above will change the type of every value that's NOT NESTED. Will get rid of all of it
# and instead provide all functionality within the two functions described below.
# Understandably this might not be as clean of a process as desired as per assignment specs, but it makes sense to me
# and appears to be straightforward in implementation

# Note - provided code appears to put every code array into a python list
# Arrays are the only items that need to be converted into python lists

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Two things need to be done: 

# Firstly, a most likely recursive function needs to be implemented that turns string number arrays
# to python lists of numbers. This will require basically visiting every single nested value and if it 
# is a string representation of an int list, convert it

# Secondly, a similarly recursive function needs to be implemented that goes through every single individual value
# (especially nested) and converts string ints, floats, bools, to their proper type

# For the first function: for each item in tokenized list, if the item is an int array, convert to a python list. 
# If the item is a code array, then recursively call the function again with code array as the passed-in value
# Returns once it reaches the end of a given sublist .

# For the second function: for each item in tokenized list, if the item is a string representation of an int, float, bool
# then convert to the proper python type. If the item is a list of any sort (code array, numerical array), then 
# recursively call upon this function again and pass in the list as the parameter. Returns once it reaches the end
# of a given sublist. 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~








# This function goes through every single value in the tokenized list, 
# and if it encounters a string representation of an array, then it calls the proper functions 
# to convert it to a python string list
# 'stringsToCorrectTypes' function will later turn these strings into python integers
def turnIntArraysToLists(tokenList):
    newArray = []
    for value in tokenList: 
        newArray.append(value)

    for i in range(0, len(newArray)): 
        # If you don't encounter a python list
        if type(newArray[i]) != list: 
            #If you encounter a string representation of an integer array, then turn it into a python list 
            # by calling convertToArray function
            if isArray(newArray[i]): 
                newArray[i] = convertToArray(newArray[i])
            else: 
                continue
        # However if you do encounter a code array, call this function again
        # The sole point of this function is turning all string representations of integer arrays ('[1 2 3]')
        # to python lists ([1,2,3]) 
        else: 
            newArray[i] = turnIntArraysToLists(newArray[i])
    
    return newArray


# This function goes through every single item in every sublist and converts it to its proper python type
# if the item is a float, int, or bool 
def stringsToCorrectTypes(tokenList): 

    returnArray = []
    for value in tokenList: 
        returnArray.append(value)
    
    for i in range(0, len(returnArray)): 
        if type(returnArray[i]) != list: 
            if isInt(returnArray[i]):
                returnArray[i] = int(returnArray[i])
            elif isFloat(returnArray[i]):
                returnArray[i] = float(returnArray[i])
            elif isTrue(returnArray[i]):
                returnArray[i] = True
            elif isFalse(returnArray[i]):
                returnArray[i] = False
        # If you do encounter a list (either int array or code array), then recursively go through that sublist
        # by again calling this function
        else: 
            returnArray[i] = stringsToCorrectTypes(returnArray[i])
    
    return returnArray

        
# This function checks if a given string is an array ('[1 2 3]')
# Returns True if it is, False otherwise
def isArray(value):

    # If the value you encounter is not a string, then it is not a string representation of an array, so return false
    if not isinstance(value, str):
        return False
    else: 
        if len(value) < 3:
            return False
        else: 
            # Increments by 2 starting from the second value, checking if each value is an integer
            # If it encounters a non-integer value, then it returns false
            for i in range(1, (len(value) - 1), 2):
                if isInt(value[i]):
                    continue
                else:
                    return False

            return True


# This function is called from 'turnIntArraysToLists' function and does the actual conversion from 
# string representation of an array to a python list of strings ('[1 2 3]' ==>  ['1', '2', '3'])
def convertToArray(value):
    returnArray = []
    tempDoubleDigit = ''
    i = 0
    while(i < (len(value))):
        if value[i] == '[' or value[i] == ']':
            i += 1
        elif value[i] == ' ':
            i += 1
            while (True):
                if value[i] == ' ' or value[i] == ']':
                    break
                else: 
                    tempDoubleDigit += value[i]
                    i += 1
            returnArray.append(tempDoubleDigit)
            tempDoubleDigit = ''
        else:
            returnArray.append(value[i])
            i += 1

    return returnArray


# Checks if a string value is representative of an integer
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Checks if a string value is representative of a floating point value
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Checks if string value is representative of the boolean value 'True'
def isTrue(value):
    if value == 'true':
        return True

# Checks if string value is representative of the boolean value 'False'
def isFalse(value):
    if value == 'false':
        return True




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
    variable = parse(tokenize(input4))
    almostFinalVariable = turnIntArraysToLists(variable)
    finalVariable = stringsToCorrectTypes(almostFinalVariable)
    print(finalVariable)
    
      