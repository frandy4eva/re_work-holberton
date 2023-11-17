import sys


def my_argv():
    sys_argv = sys.argv
    num_argv = len(sys_argv) - 1

    if num_argv == 0:
        print("0 arguments.")
    else:
        print(f"{num_argv} {'argument:' if num_argv == 1 else 'arguments:'}")

        counter = 1
        for elm in sys_argv[1:]:
            print(f"{counter}: {elm}")
            counter += 1

# Example usage:


if __name__ == '__main__':
    my_argv()
