# -*- coding: utf-8 -*-


# Brandon Campbell
# Fall 2018 CPTS 355
# HW 4 Part 1

# ------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations

import re
op_stack = []  # assuming top of the stack is the end of the list
dict_stack = []  # assuming top of the stack is the end of the list


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
# now define functions to push and pop dictionaries on the dictstack, to define
# name, and to lookup a name


def dict_pop():

    global dict_stack

    if len(dict_stack) < 1:
        print('Can\'t pop as there are no items in the dict stack!')
        return
    else:
        return_value = dict_stack[-1]
        del dict_stack[-1]
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

    global dict_stack

    dict_to_push = {name: value}

    if len(dict_stack) < 1:
        dict_stack.append({name: value})
    else:
        dict_stack[-1].update(dict_to_push)


# add name:value to the top dictionary in the dictionary stack. (Keep the ‘/’ in
# name when you add it to the top dictionary) Your psDef function should pop the
# name and value from operand stack and call the “define” function.

def lookup(name):

    global dict_stack
    for item in reversed(dict_stack):
        for key in item:
            if key == name:
                return item[key]
                break

    print('No dictionary with that name in the dictionary stack!')


# return the value associated with name.
# What is your design decision about what to do when there is no definition for
# name? If “name” is not defined, your program should not break, but should
# give an appropriate error message.

# --------------------------- 15% -------------------------------------
# Arithmetic and comparison operators: define all the arithmetic and
# comparison operators here -- add, sub, mul, div, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters and
# types of the parameters are correct.

def add():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        # Checks if the first value popped is an integer. If so, then it continues
        if type(val_1) == int or type(val_1) == float:

            val_2 = op_pop()
            # If both are integers, then perform the operation. Otherwise, push all values back to stack
            if type(val_2) == int or type(val_2) == float:
                return_val = val_1 + val_2
                op_push(return_val)
            else:
                op_push(val_2)
                op_push(val_1)
                print('One or more of the values was not an integer!')
        else:
            op_push(val_1)
            print('One or more of the values was not an integer')
    else:
        print('Not enough values in stack to perform the operation!')


def sub():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        # Checks if the first value popped is an integer. If so, then it continues
        if type(val_1) == int or type(val_1) == float:

            val_2 = op_pop()
            # If both are integers, then perform the operation. Otherwise, push all values back to stack
            if type(val_2) == int or type(val_2) == float:
                return_val = val_2 - val_1
                op_push(return_val)
            else:
                op_push(val_2)
                op_push(val_1)
                print('One or more of the values was not an integer!')
        else:
            op_push(val_1)
            print('One or more of the values was not an integer')
    else:
        print('Not enough values in stack to perform the operation!')


def mul():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        # Checks if the first value popped is an integer. If so, then it continues
        if type(val_1) == int or type(val_1) == float:

            val_2 = op_pop()
            # If both are integers, then perform the operation. Otherwise, push all values back to stack
            if type(val_2) == int or type(val_2) == float:
                return_val = val_1 * val_2
                op_push(return_val)
            else:
                op_push(val_2)
                op_push(val_1)
                print('One or more of the values was not an integer!')
        else:
            op_push(val_1)
            print('One or more of the values was not an integer')
    else:
        print('Not enough values in stack to perform the operation!')


def div():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        # Checks if the first value popped is an integer. If so, then it continues
        if type(val_1) == int or type(val_1) == float:

            val_2 = op_pop()
            # If both are integers, then perform the operation. Otherwise, push all values back to stack
            if type(val_2) == int or type(val_2) == float:
                return_val = float(val_2)/float(val_1)
                op_push(return_val)
            else:
                op_push(val_2)
                op_push(val_1)
                print('One or more of the values was not an integer!')
        else:
            op_push(val_1)
            print('One or more of the values was not an integer')
    else:
        print('Not enough values in stack to perform the operation!')


def eq():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        # Checks if the first value popped is an integer. If so, then it continues
        if type(val_1) == int or type(val_1) == float:

            val_2 = op_pop()
            # If both are integers, then perform the operation. Otherwise, push all values back to stack
            if type(val_2) == int or type(val_2) == float:
                return_val = val_1 == val_2
                op_push(return_val)
            else:
                op_push(val_2)
                op_push(val_1)
                print('One or more of the values was not an integer!')
        else:
            op_push(val_1)
            print('One or more of the values was not an integer')
    else:
        print('Not enough values in stack to perform the operation!')


def lt():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        # Checks if the first value popped is an integer. If so, then it continues
        if type(val_1) == int or type(val_1) == float:

            val_2 = op_pop()
            # If both are integers, then perform the operation. Otherwise, push all values back to stack
            if type(val_2) == int or type(val_2) == float:
                return_val = val_2 < val_1
                op_push(return_val)
            else:
                op_push(val_2)
                op_push(val_1)
                print('One or more of the values was not an integer!')
        else:
            op_push(val_1)
            print('One or more of the values was not an integer')
    else:
        print('Not enough values in stack to perform the operation!')


def gt():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        # Checks if the first value popped is an integer. If so, then it continues
        if type(val_1) == int or type(val_1) == float:

            val_2 = op_pop()
            # If both are integers, then perform the operation. Otherwise, push all values back to stack
            if type(val_2) == int or type(val_2) == float:
                return_val = val_1 > val_2
                op_push(return_val)
            else:
                op_push(val_2)
                op_push(val_1)
                print('One or more of the values was not an integer!')
        else:
            op_push(val_1)
            print('One or more of the values was not an integer')
    else:
        print('Not enough values in stack to perform the operation!')


# --------------------------- 15% -------------------------------------
# Array operators: define the array operators length, get

def length():

    global op_stack

    # Get the array that is at the top of the stack
    arr = op_pop()

    # Get its length and then push it to the stack
    arr_length = len(arr)
    op_push(arr_length)


def get():

    global op_stack

    # Get the index and get the array
    ind = op_pop()
    arr = op_pop()

    # Get Array[index] and push to the stack
    push_val = arr[ind]
    op_push(push_val)


# --------------------------- 15% -------------------------------------
# Boolean operators: define the boolean operators psAnd, psOr, psNot
# Remember that these take boolean operands only. Anything else is an error

def ps_and():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        # Checks if the first value popped is a bool. If so, then it continues
        if type(val_1) == bool:

            val_2 = op_pop()
            # If both are bool, then perform the operation. Otherwise, push all values back to stack
            if type(val_2) == bool:
                return_val = val_1 and val_2
                op_push(return_val)
            else:
                op_push(val_2)
                op_push(val_1)
                print('One or more of the values was not an integer!')
        else:
            op_push(val_1)
            print('One or more of the values was not an integer')
    else:
        print('Not enough values in stack to perform the operation!')


def ps_or():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        # Checks if the first value popped is a bool. If so, then it continues
        if type(val_1) == bool:

            val_2 = op_pop()
            # If both are bools, then perform the operation. Otherwise, push all values back to stack
            if type(val_2) == bool:
                return_val = val_1 or val_2
                op_push(return_val)
            else:
                op_push(val_2)
                op_push(val_1)
                print('One or more of the values was not an integer!')
        else:
            op_push(val_1)
            print('One or more of the values was not an integer')
    else:
        print('Not enough values in stack to perform the operation!')


def ps_not():

    global op_stack

    # Checks if there are enough operands in the stack
    if len(op_stack) >= 1:

        val_1 = op_pop()
        # Checks if the first value popped is a bool. If so, then it continues
        if type(val_1) == bool:
            return_value = not val_1
            op_push(return_value)
        else:
            op_push(val_1)
            print('The value at the top of the stack was not a bool!')
    else:
        print('Not enough values in stack to perform the operation!')

# --------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, exch, pop, copy,
# clear, stack


def dup():

    global op_stack

    # Check if the stack is empty
    if len(op_stack) >= 1:

        # Get the top value and then push it to the stack
        top_val = op_stack[-1]
        op_push(top_val)

    else:
        print("Cannot perform the operation as the stack is empty!")


def exch():

    global op_stack

    # Check if there are at least 2 values in the stack
    if len(op_stack) >= 2:

        val_1 = op_pop()
        val_2 = op_pop()

        # Just reverse the order of them by pushing in different order
        op_push(val_1)
        op_push(val_2)

    else:
        print("There are not enough values in the stack to perform this operation")


def pop():

    # Is this not already accomplished with the op_pop() function from earlier?
    op_pop()


def copy():

    global op_stack

    # Get the top value of the stack which represents the amount of things to copy
    elements_to_copy = op_pop()

    # Check if there enough elements to perform the operation
    if len(op_stack) < elements_to_copy:
        op_push(elements_to_copy)
        print("There are not enough elements in the stack to perform this operation")

    else:
        # Reverse this so you can traverse from the back
        new_array = list(reversed(op_stack))[:elements_to_copy]

        # The array of items to copy will be reverse order of what we want, so reverse it and push each value
        for value in list(reversed(new_array)):
            op_push(value)


def clear():

    global op_stack

    # Just clear everything
    del op_stack[:]


def stack():

    global op_stack

    print("TOP")
    print("~~~")

    for item in list(reversed(op_stack)):
        print(item)

    print("~~~")
    print("BOTTOM")

# --------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in
# Python.
# Note: The psDef operator will pop the value and name from the opstack and
# call your own "define" operator (pass those values as parameters). Note that
# psDef()won't have any parameters.


def ps_dict():

    global op_stack

    if len(op_stack) > 0:

        op_pop()
        new_dict = {}
        op_push(new_dict)

    else:
        print("Operation cannot be performed as the operand stack is empty")


def begin():

    global op_stack

    if len(op_stack) < 1:
        print("There aren't any values on the operand stack ")

    else:
        value_1 = op_pop()

        if type(value_1) == dict:
            dict_push(value_1)
        else:
            op_push(value_1)
            print("The value at the top of the operand stack is not a dictionary.")


def end():

    global dict_stack

    if len(dict_stack) < 1:
        print("There aren't any values on the dictionary stack ")

    else:
        dict_pop()


def ps_def():

    global op_stack

    # Check if there are enough values on the operand stack and if values are in the correct format
    if len(op_stack) < 2:
        print("There are not enough values on the operand stack to perform the operation")
        return

    # Get the first two variables from the operand stack
    value_1 = op_pop()
    value_2 = op_pop()

    if value_2[0] != '/':
        op_push(value_2)
        op_push(value_1)
        print("The entry is not in the correct format")

        # Take the '/' from the name and then add to the dictionary at the top of the dict stack
    else:
        new_value_2 = value_2[1:]
        define(new_value_2, value_1)


# ------- Part 1 TEST CASES--------------

# The assignment says that the '/' should remain when implementing define
# So the given test function is incorrect on the basis of that

def test_define1():
    define("/n1", 4)
    if lookup("/n1") != 4:
        return False
    return True

def test_define2():
    define("/n1", 4)
    define("/n1", 5.0)
    if lookup("/n1") != 5.0:
        return False
    return True


def test_lookup():
    op_push("/n1")
    op_push(3)
    ps_def()
    if lookup("n1") != 3:
        return False
    return True


# Arithmatic operator tests
def test_add():
    op_push(1)
    op_push(2)
    add()
    if op_pop() != 3:
        return False
    return True


def test_sub():
    op_push(10)
    op_push(4.5)
    sub()
    if op_pop() != 5.5:
        return False
    return True


def test_mul():
    op_push(2)
    op_push(4.5)
    mul()
    if op_pop() != 9:
        return False
    return True


def test_div():
    op_push(10)
    op_push(4)
    div()
    if op_pop() != 2.5:
        return False
    else:
        return True


# Comparison operators tests
def test_eq():
    op_push(6)
    op_push(6)
    eq()
    if op_pop() is False:
        return False
    return True


def test_lt():
    op_push(3)
    op_push(6)
    lt()
    if op_pop() is False:
        return False
    return True


def test_gt():
    op_push(4)
    op_push(5)
    gt()
    if op_pop() is False:
        return False
    return True


# boolean operator tests
def test_ps_and():
    op_push(True)
    op_push(False)
    ps_and()
    if op_pop() is True:
        return False
    return True


def test_ps_or():
    op_push(True)
    op_push(False)
    ps_or()
    if op_pop() is False:
        return False
    return True


def test_ps_not():
    op_push(True)
    ps_not()
    if op_pop() is True:
        return False
    return True


# Array operator tests
def test_length():
    op_push([1, 2, 3, 4, 5])
    length()
    if op_pop() != 5:
        return False
    return True


def test_get():
    op_push([1, 2, 3, 4, 5])
    op_push(4)
    get()
    if op_pop() != 5:
        return False
    return True


# stack manipulation functions
def test_dup():
    op_push(10)
    dup()
    if op_pop() != op_pop():
        return False
    return True


def test_exch():
    op_push(10)
    op_push("/x")
    exch()
    if op_pop() != 10 and op_pop() != "/x":
        return False
    return True


def test_pop():
    l1 = len(op_stack)
    op_push(10)
    pop()
    l2 = len(op_stack)
    if l1 != l2:
        return False
    return True


def test_copy():
    op_push(1)
    op_push(2)
    op_push(3)
    op_push(4)
    op_push(5)
    op_push(2)
    copy()
    if op_pop() != 5 and op_pop() != 4 and op_pop() != 5 and op_pop() != 4 and op_pop() != 3 and op_pop() != 2:
        return False
    return True


def test_clear():
    op_push(10)
    op_push("/x")
    clear()
    if len(op_stack) != 0:
        return False
    return True


# dictionary stack operators
def test_dict():
    op_push(1)
    ps_dict()
    if op_pop() != {}:
        return False
    return True


def test_begin_end():
    op_push("/x")
    op_push(3)
    ps_def()
    op_push({})
    begin()
    op_push("/x")
    op_push(4)
    ps_def()
    end()
    if lookup("x") != 3:
        return False
    return True


def test_psdef():
    op_push("/x")
    op_push(10)
    ps_def()
    if lookup("x") != 10:
        return False
    return True


def test_psdef2():
    op_push("/x")
    op_push(10)
    ps_def()
    op_push(1)
    ps_dict()
    begin()
    if lookup("x") != 10:
        end()
        return False
    end()
    return True

def test_div_inputs(): 
    op_push("/x")
    op_push(10)
    div()
    print(op_stack)
    if op_stack == ["/x", 10]:
        return True
    else: 
        return False



def main_part1():

    test_cases = [('define1', test_define1()), ('define2', test_define2()), ('lookup', test_lookup()), ('add', test_add()),
                  ('sub', test_sub()), ('mul', test_mul()),('div', test_div()), ('eq', test_eq()),
                  ('lt', test_lt()), ('gt', test_gt()), ('psAnd', test_ps_and()), ('psOr', test_ps_or()),
                  ('psNot', test_ps_not()), ('length', test_length()), ('get', test_get()), ('dup', test_dup()),
                  ('exch', test_exch()), ('pop', test_pop()), ('copy', test_copy()), ('clear', test_clear()),
                  ('dict', test_dict()), ('begin', test_begin_end()), ('psDef', test_psdef()), ('psDef2', test_psdef2()), 
                  ('divInputs', test_div_inputs())]

    failed_tests = [test_name for (test_name, test_proc) in test_cases if test_proc is False]

    if failed_tests:
        return 'Some tests failed', failed_tests
    else:
        return 'You passed all of the tests!!'


if __name__ == '__main__':
    print(main_part1())



