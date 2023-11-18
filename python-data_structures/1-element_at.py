"""Retrieve an element from a list."""


def element_at(my_list, idx):
    """Returns element at a specific index of my_list based on idx

    Args:
    - my_list (list): Contains a list of values.
    - idx (int): The index to retrieve the value from.

    Returns:
    The value at the giving index of my_list.
    Returns None is index is negative or index is out of bounds.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
