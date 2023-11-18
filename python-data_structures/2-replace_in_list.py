"""Replace an element of a list at a specific position."""


def replace_in_list(my_list, idx, element):
    """Replace the element in my_list at the specified index with a new value.

    Args:
    - my_list (list): The list containing values.
    - idx (int): The index at which the element is to be replaced.
    - element: The new value to be inserted.

    Returns:
    list: The modified list after the replacement.
    list: The original list if the given index is out of bounds or negative.
    """
    if not (0 <= idx < len(my_list)):
        return my_list
    my_list[idx] = element
    return my_list
