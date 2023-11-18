"""Print all integers of a list in reverse order"""


def print_reversed_list_integer(my_list=[]):

    if isinstance(my_list, list):
        for val in my_list[::-1]:
            print(val)
