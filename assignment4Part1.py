# Brandon Campbell
# Fall 2018 CPTS 355
# HW 4 Part 1

# ------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations

op_stack = []


def op_pop():

    global op_stack

    if len(op_stack) < 1:
        print('Can\'t pop as there are no items in the op stack!')
        return
    else:
        return_value = op_stack[-1] # Retain last element data
        del op_stack[-1]
        return return_value


def op_push(value):

    global op_stack

    op_stack.append(value)


# -------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dict_stack = []

# now define functions to push and pop dictionaries on the dictstack, to define
# name, and to lookup a name


def dict_pop():

    global dict_stack

    if len(dict_stack) < 1:
        print('Can\'t pop as there are no items in the dict stack!')
        return
    else:
        return_value = op_stack[-1]
        del op_stack[-1]
        return return_value


# dictPop pops the top dictionary from the dictionary stack.

def dict_push(d):

    global dict_stack

    dict_stack.append(d)


# dictPush pushes a new dictionary to the dictstack. Note that, your interpreter
# will call dictPush only when Postscript “begin” operator is called. “begin”
# should pop the empty dictionary from the opstack and push it onto the dictstack
# by calling dictPush. You may either pass this dictionary (which you popped from
# opstack) to dictPush as a parameter or just simply push a new empty dictionary
# in dictPush.

def define(name, value):
    pass


# add name:value to the top dictionary in the dictionary stack. (Keep the ‘/’ in
# name when you add it to the top dictionary) Your psDef function should pop the
# name and value from operand stack and call the “define” function.

def lookup(name):
    pass


# return the value associated with name.
# What is your design decision about what to do when there is no definition for
# name? If “name” is not defined, your program should not break, but should
# give an appropriate error message.

# --------------------------- 15% -------------------------------------
# Arithmetic and comparison operators: define all the arithmetic and
# comparison operators here -- add, sub, mul, div, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters and
# types of the parameters are correct.

# --------------------------- 15% -------------------------------------
# Array operators: define the array operators length, get
#--------------------------- 15% -------------------------------------
# Boolean operators: define the boolean operators psAnd, psOr, psNot
# Remember that these take boolean operands only. Anything else is an error

# --------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, exch, pop, copy,
# clear, stack

# --------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in
# Python.
# Note: The psDef operator will pop the value and name from the opstack and
# call your own "define" operator (pass those values as parameters). Note that
# psDef()won't have any parameters.