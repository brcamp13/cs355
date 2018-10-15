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




