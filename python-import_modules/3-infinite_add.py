
import sys

if __name__ == '__main__':
    def sum_argm(argv: int):
        """Calculate the sum of all arguments

        Args:
        - argm (int): Argument as integer

        Returns:
        int: The result of adding all the arguments
        """
        counter = 0
        for num in sys.argv[1:]:
            counter += sys.argv[num + 1]
        return counter
