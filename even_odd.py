"""Reorder array so that even integer entries appear first."""


def even_odd(arr):
    """Reorder so that even integers appear first.

    Solve without increasing storage.
    input: list of integers
    output: even integers, then odd integers.
    """
    next_even, next_odd = 0, len(arr) - 1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1
    return arr
