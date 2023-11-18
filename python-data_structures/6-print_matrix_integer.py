"""Print matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print("{}".format(matrix[row][col]), end=' ')
            if col != (len(matrix[row]) - 1):
                print(' ', end='')
        print('')
