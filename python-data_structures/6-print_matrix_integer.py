"""Print matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in row:
            print("{}".format(elem), end=' ')
        print('')
