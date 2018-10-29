# Brandon Campbell
# Fall 2018 CPTS 355
# HW 4 Part 1

# ------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations


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
                return_val = val_2/val_1
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
                return_val = val_2 > val_1
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
    pass
    # Is this not already accomplished with the op_pop() function from earlier?


def copy():

    global op_stack

    # Get the top value of the stack which represents the amount of things to copy
    elements_to_copy = op_pop()

    # Check if there enough elements to perform the operation
    if len(op_stack) < elements_to_copy():
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
    op_stack.clear()


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


op_stack = []  # assuming top of the stack is the end of the list
dict_stack = []  # assuming top of the stack is the end of the list


# ------- Part 1 TEST CASES--------------
def test_define():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True


def test_lookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True


# Arithmatic operator tests
def test_add():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True


def test_sub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True


def test_mul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True


def test_div():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True


# Comparison operators tests
def test_eq():
    opPush(6)
    opPush(6)
    eq()
    if opPop() != True:
        return False
    return True


def test_lt():
    opPush(3)
    opPush(6)
    lt()
    if opPop() != True:
        return False
    return True


def test_gt():
    opPush(3)
    opPush(6)
    gt()
    if opPop() != False:
        return False
    return True


# boolean operator tests
def test_ps_and():
    opPush(True)
    opPush(False)
    psAnd()
    if opPop() != False:
        return False
    return True


def test_ps_or():
    opPush(True)
    opPush(False)
    psOr()
    if opPop() != True:
        return False
    return True


def test_ps_not():
    opPush(True)
    psNot()
    if opPop() != False:
        return False
    return True


# Array operator tests
def test_length():
    opPush([1, 2, 3, 4, 5])
    length()
    if opPop() != 5:
        return False
    return True


def test_get():
    opPush([1, 2, 3, 4, 5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True


# stack manipulation functions
def test_dup():
    opPush(10)
    dup()
    if opPop() != opPop():
        return False
    return True


def test_exch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop() != 10 and opPop() != "/x":
        return False
    return True


def test_pop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2 = len(opstack)
    if l1 != l2:
        return False
    return True


def test_copy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop() != 5 and opPop() != 4 and opPop() != 5 and opPop() != 4 and opPop() != 3 and opPop() != 2:
        return False
    return True


def test_clear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack) != 0:
        return False
    return True


# dictionary stack operators
def test_dict():
    opPush(1)
    psDict()
    if opPop() != {}:
        return False
    return True


def test_begin_end():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x") != 3:
        return False
    return True


def test_psdef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x") != 10:
        return False
    return True


def test_psdef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x") != 10:
        end()
        return False
    end()
    return True


def main_part1():
    testCases = [('define', test_define), ('lookup', testLookup), ('add', testAdd), ('sub', testSub), ('mul', testMul),
                 ('div', testDiv), \
                 ('eq', testEq), ('lt', testLt), ('gt', testGt), ('psAnd', testPsAnd), ('psOr', testPsOr),
                 ('psNot', testPsNot), \
                 ('length', testLength), ('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop),
                 ('copy', testCopy), \
                 ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef),
                 ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return 'Some tests failed', failedTests
    else:
        return 'All part-1 tests OK'


if __name__ == '__main__':
    print(main_part1())



