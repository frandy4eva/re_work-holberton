"""Remove all characters `c` and `C` from a string"""


def no_c(my_string):
    new_string = ' '
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            new_string += letter
    print(new_string)
