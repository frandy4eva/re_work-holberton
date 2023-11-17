import hidden_4
if __name__ == '__main__':
    """Print all names defined in hidden_4 that don't contain `__`"""
    names = dir(hidden_4)

    for name in names:
        if '__' not in name:
            print(name)
