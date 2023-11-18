"""Find the biggest integer of a list"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    counter = (float('-inf'))
    for num in my_list:
        if num > counter:
            counter = num
    return counter
