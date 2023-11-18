"""Print all integers of a list"""


def print_list_integer(my_list=[]):
    """Print all my-list values each per line

    Args:
    - my_list (list): A list containing integers

    Returns:
    No returns
    """
    for num in my_list:
        print("{}".format(num))
