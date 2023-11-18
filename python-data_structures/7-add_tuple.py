"""Add two tuples"""


def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure the tuples have at least two elements
    tuple_a = (tuple_a[0] if len(tuple_a) > 0 else 0,
               tuple_a[1] if len(tuple_a) > 1 else 0)
    tuple_b = (tuple_b[0] if len(tuple_b) > 0 else 0,
               tuple_b[1] if len(tuple_b) > 1 else 0)

    # Return a tuple with the sum of corresponding elements
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
