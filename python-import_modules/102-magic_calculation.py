def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        calc = add(a, b)
        for num in range(4, 6):
            calc = add(a, num)
        return num
    else:
        return sub(a, b)
