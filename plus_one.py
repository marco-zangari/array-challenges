"""Return updated integer of integer + 1."""


def increment_one(arr):
    """Return incremented arr by one."""
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if i != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[i] == 10:
        arr[0] = 1
        arr.append(0)
    return arr
