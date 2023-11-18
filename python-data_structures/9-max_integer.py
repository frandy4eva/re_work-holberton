"""Find the biggest integer of a list"""


def max_integer(my_list=[]):
    if not my_list:
        return None

    counter = (float('-inf'))
    for num in my_list:
        if num > counter:
            counter = num
    return counter
