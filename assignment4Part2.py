# Brandon Campbell
# Fall 2018 CS 355
# Assignment 4 part 2

import assignment4Part1 as assignment1Functions
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


def psIf():
    codeArray = assignment1Functions.op_pop()
    boolValue = assignment1Functions.op_pop()
    if boolValue == True: 
        interpretSPS(codeArray)
    


def psIfelse(): 

    codeArray2 = assignment1Functions.op_pop()
    codeArray1 = assignment1Functions.op_pop()
    boolValue = assignment1Functions.op_pop()

    if boolValue == True: 
        interpretSPS(codeArray1)
    else: 
        interpretSPS(codeArray2)

def psFor(): 

    initialValue = assignment1Functions.op_pop()
    incrementValue = assignment1Functions.op_pop()
    finalValue = assignment1Functions.op_pop()
    codeArray = assignment1Functions.op_pop()

    while(initialValue <= finalValue): 
        assignment1Functions.op_push(initialValue)
        interpretSPS(codeArray)
        initialValue += incrementValue

    

def psForAll():
    procedure = assignment1Functions.op_pop()
    intArray = assignment1Functions.op_pop()
    for item in intArray: 
        assignment1Functions.op_push(item)
        interpretSPS(procedure) 
        



# Pretty much go through the code array and whenever you lookup a code array, recursively call this function
def interpretSPS(code): # code is a code array

    postscriptOperations = ['add', 'sub', 'mul', 'div', 'eq', 'lt', 'gt', 'and', 'or', 'not', 'if', 'ifelse'
    ,'for', 'forall', 'length', 'get', 'dup', 'exch', 'pop', 'copy', 'clear', 'def', 'stack']

    for item in code: 
        if isinstance(item, str):
            # If the item is a name declaration
            if item[0] == '/':
                assignment1Functions.op_push(item)
                continue
            
            # If the item is a postscript operation
            elif item in postscriptOperations:
                if item == 'add':
                    assignment1Functions.add() 
                elif item == 'sub': 
                    assignment1Functions.sub()
                elif item == 'mul': 
                    assignment1Functions.mul()
                elif item == 'div': 
                    assignment1Functions.div()
                elif item == 'eq':
                    assignment1Functions.eq() 
                elif item == 'lt':
                    assignment1Functions.lt() 
                elif item == 'gt': 
                    assignment1Functions.gt()
                elif item == 'and': 
                    assignment1Functions.ps_and()
                elif item == 'or': 
                    assignment1Functions.ps_or()
                elif item == 'not':
                    assignment1Functions.ps_not() 
                # Recursive
                elif item == 'if': 
                    psIf()
                    continue
                # Recursive
                elif item == 'ifelse': 
                    psIfElse()
                    continue
                # Recursive
                elif item == 'for':
                    psFor()
                    continue
                # Recursive 
                elif item == 'forall': 
                    psForAll()
                    continue

                elif item == 'length':
                    assignment1Functions.length() 
                elif item == 'get':
                    assignment1Functions.get() 
                elif item == 'dup': 
                    assignment1Functions.dup()
                elif item == 'exch':
                    assignment1Functions.exch() 
                elif item == 'pop':
                    assignment1Functions.pop() 
                elif item == 'copy':
                    assignment1Functions.copy() 
                elif item == 'clear':
                    assignment1Functions.clear() 
                elif item == 'def': 
                    assignment1Functions.ps_def()
                elif item == 'stack':
                    assignment1Functions.stack() 

            # If the item is a name lookup
            # If lookup yields a code array, then execute that code array. 
            # Otherwise, I don't believe you do anything unless she wants the value to be printed
            else:
                value = assignment1Functions.lookup(item)
                if type(value) == list: 
                    if all(isinstance(x, int) for x in value):
                        interpretSPS(value)
                    else: 
                        continue
                else: 
                    continue
        
        elif type(item) == list: 
            assignment1Functions.op_push(item)
            continue

        elif type(item) == int or type(item) == float: 
            assignment1Functions.op_push(item)
            continue

    return




def interpreter(s): # s is a string

    # Input 3 works, but not 1 or 2 or 4
    # Time to debug...

    variable = parse(tokenize(s))
    almostFinalVariable = turnIntArraysToLists(variable)
    finalVariable = stringsToCorrectTypes(almostFinalVariable)
    interpretSPS(finalVariable)


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
    interpreter(input3)
    
      