# Brandon Campbell
# Cpts 355 Fall 2018
# HW 3

# ~~~~~~~~~IMPORTS~~~~~~~~
from functools import reduce
from collections import Counter
# ~~~~~~~~~~~~~~~~~~~~~~~~

# (1a)


def add_dict(hours_worked):

    # I understand that you didn't want this hardcoded, but makes readability way better
    return_dict = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}

    # If you encounter a given day of the week, increment its return dictionary with key
    for a, b in hours_worked.items():
        for c, d in b.items():
            if c is 'Mon':
                return_dict['Mon'] += d
            elif c is 'Tue':
                return_dict['Tue'] += d
            elif c is 'Wed':
                return_dict['Wed'] += d
            elif c is 'Thu':
                return_dict['Thu'] += d
            elif c is 'Fri':
                return_dict['Fri'] += d
            elif c is 'Sat':
                return_dict['Sat'] += d
            elif c is 'Sun':
                return_dict['Sun'] += d

    return return_dict


# This helper function adds up the keys in two dictionaries of dictionaries


def helper_add_dict_n(list_item_1, list_item_2):

    # Using counters (basically a subclass of dict) allows for simple addition
    first = Counter(list_item_1)
    second = Counter(list_item_2)

    return first + second


# (1b)


def add_dict_n(list_of_dicts):

    # This applies the add dict function to each list entry
    mapped_dict = list(map(add_dict, list_of_dicts))

    # Utilizing a counter so dictionary + dictionary operation can be performed in the manner that works with reduce
    # Empty counter acts as the base condition for reduce
    empty_counter = Counter()
    return dict(reduce(helper_add_dict_n, mapped_dict, empty_counter))


# (2a)


def lookup_val(list_of_dicts, search_key):

    for item in reversed(list_of_dicts):    # Reversing the input makes it so you traverse from the 'end'
        for key, value in item.items():
            if key == search_key:
                return value
    print("Key not found")
    return None


# (2b)


def lookup_val_2(tuple_list, search_key):

    # Counter will keep track of which index you are currently at (as you are required to skip the 2nd and 4th index
    # (3rd and 5th item))
    counter = len(tuple_list) - 1
    dictionaries = reversed([item[1] for item in tuple_list])  # Get 2nd value of each tuple in a new list, then reverse
    for dictionary in dictionaries:
        for key, value in dictionary.items():
            if counter == 2 or counter == 4:    # If you are at the dictionary to skip, then skip
                counter -= 1
                continue
            elif key == search_key:
                return value
            else:
                counter -= 1

    return None


# (3)

# Looking into why there's some strange output for some test cases
def num_paths(m, n, blocks):

    if(m, n) in blocks:
        return 0
    elif m == 1 or n == 1:
        return 1
    else:
        return num_paths(m - 1, n, blocks) + num_paths(m, n - 1, blocks)


# (4)
# Each substring in from the given string will be found, then tested to see if palindrome
def palindromes(input_string):

    # Removes all duplicates within a given list
    def remove_duplicates(string_list):

        return_val = []
        for item in string_list:
            if item not in return_val:
                return_val.append(item)
            else:
                continue

        return return_val

    # Get all substrings within the input string
    list_of_substrings = \
        list((input_string[x:y] for x in range(len(input_string)) for y in range(x + 1, len(input_string) + 1)))

    # The lambda function checks if a string == its reverse (if it's a palindrome)
    return_list = list(filter(lambda x: x == x[::-1], list_of_substrings))

    # Alphabetical order as per assignment specs
    return_list.sort()

    # Remove duplicates as per assignment specs
    final_return_list = remove_duplicates(return_list)

    return final_return_list


# ~~~~~~~~TEST FUNCTIONS~~~~~~~~


def test_add_dict():

    test1 = (add_dict({'355': {'Mon': 3, 'Wed': 2, 'Sat': 2}, '360': {'Mon': 3, 'Tue': 2, 'Wed': 2, 'Fri': 10}})) ==\
            ({'Mon': 6, 'Tue': 2, 'Wed': 4, 'Thu': 0, 'Fri': 10, 'Sat': 2, 'Sun': 0})

    test2 = (add_dict({'321': {'Tue': 2, 'Wed': 2, 'Thu': 3}, '322': {'Tue': 1, 'Thu': 5, 'Sat': 2}})) ==\
            ({'Mon': 0, 'Tue': 3, 'Wed': 2, 'Thu': 8, 'Fri': 0, 'Sat': 2, 'Sun': 0})

    print(test1)
    print(test2)


def test_add_dict_n():

    test1 = (add_dict_n(

        [{'355': {'Mon': 3, 'Wed': 2, 'Sat': 2}, '360': {'Mon': 3, 'Tue': 2, 'Wed': 2, 'Fri': 10},
          '321': {'Tue': 2, 'Wed': 2, 'Thu': 3}, '322': {'Tue': 1, 'Thu': 5, 'Sat': 2}},
         {'322': {'Mon': 2}, '360': {'Thu': 2, 'Fri': 5}, '321': {'Mon': 1, 'Sat': 3}},
         {'355': {'Sun': 8}, '360': {'Fri': 5}, '321': {'Mon': 4}, '322': {'Sat': 3}}]) ==

        {'Mon': 13, 'Tue': 5, 'Wed': 6, 'Thu': 10, 'Fri': 20, 'Sat': 10, 'Sun': 8}

    )
    test2 = (add_dict_n(
        [{'355': {'Mon': 3, 'Wed': 7, 'Sat': 2}, '360': {'Mon': 3, 'Tue': 2, 'Wed': 2, 'Fri': 10},
          '321': {'Tue': 2, 'Wed': 2, 'Thu': 3}, '322': {'Tue': 1, 'Thu': 5, 'Sat': 2}},
         {'322': {'Mon': 2}, '360': {'Thu': 2, 'Fri': 3}, '321': {'Mon': 1, 'Sat': 3}},
         {'355': {'Sun': 8}, '360': {'Fri': 5}, '321': {'Mon': 4}, '322': {'Sat': 12}}]) ==

             {'Mon': 13, 'Tue': 5, 'Wed': 11, 'Thu': 10, 'Fri': 18, 'Sat': 19, 'Sun': 8}

             )

    print(test1)
    print(test2)


def test_lookup_val():

    test1 = ((lookup_val([{"x": 1, "y": True, "z": "found"}, {"x": 2}, {"y": False}], "x")) == 2)
    test2 = ((lookup_val([{"x": 1, "y": True, "z": "found"}, {"x": 2}, {"y": False}], "y")) == (not True))
    test3 = ((lookup_val([{"H": "Hello World", "y": True, "z": "found"}, {"x": 2}, {"y": False}], "H")) == "Hello World")

    print(test1)
    print(test2)
    print(test3)


def test_lookup_val_2():

    test1 = ((lookup_val_2([(0, {"x": 0, "y": True, "z": "zero"}), (0, {"x": 1}), (1, {"y": False}),
                            (1, {"x": 3, "z": "three"}), (2, {})], "x")) == 1)

    test2 = ((lookup_val_2([(0, {"x": 0, "y": True, "z": "zero"}), (0, {"x": 1}), (1, {"y": False}),
                            (1, {"x": 3, "z": "three"}), (2, {})], "z")) == "three")

    test3 = ((lookup_val_2([(0, {"x": 0, "y": True, "z": "zero"}), (0, {"x": 1}), (1, {"y": False}),
                            (1, {"x": 3, "z": "three"}), (2, {})], "y")) == True)

    print(test1)
    print(test2)
    print(test3)


def test_palindrome():

    test1 = ((palindromes('cabbbaccab')) == (['a', 'abbba', 'acca', 'b', 'baccab', 'bb', 'bbb', 'c', 'cabbbac', 'cc']))
    test2 = ((palindromes('racecar')) == (['a', 'aceca', 'c', 'cec', 'e', 'r', 'racecar']))
    test3 = ((palindromes('bacdcabdbcdc')) == (['a', 'acdca', 'b', 'bacdcab', 'bdb', 'c', 'cdc', 'd']))

    print(test1)
    print(test2)
    print(test3)


def num_paths_test():

    test1 = ((num_paths(2, 2, [(2, 1)])) == 1)
    test2 = ((num_paths(3, 3, [(2, 1)])) == 4)

    print(test1)
    print(test2)


def run_all_tests():

    print("add_dict test")
    test_add_dict()
    print("add_dict_n test")
    test_add_dict_n()
    print("lookup_val test")
    test_lookup_val()
    print("lookup_val_2 test")
    test_lookup_val_2()
    print("num_paths test")
    num_paths_test()
    print("palindrome test")
    test_palindrome()