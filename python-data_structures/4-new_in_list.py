"""Replace an element in a list at giving position without modifying the original list"""


def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        my_list_copy = my_list[:]

        if not (0 <= idx < len(my_list)):
            return my_list_copy
        my_list_copy[idx] = element
        return my_list_copy
