
import sys


def sum_argm():
    """Calculate the sum of all arguments

    Args:
    - argm (int): Argument as integer

    Returns:
    int: The result of adding all the arguments
    """
    counter = 0
    sys_argv = sys.argv
    for num in sys_argv[1:]:
        counter += sys_argv[num + 1]
    return counter


if __name__ == '__main__':
    sum_argm()
