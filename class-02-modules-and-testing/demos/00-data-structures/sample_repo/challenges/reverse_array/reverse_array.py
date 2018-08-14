def reverse_array(arr):
    """Function which accepts List as argument and returns the same list argument in reverse

    Args:
        arr (object): list
    """
    # if type(arr) is not list:
    #     raise TypeError('Gnarf - there was an error')

    mid = len(arr) // 2
    p1, p2 = 0, -1

    for _ in range(mid):
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1

    return arr

