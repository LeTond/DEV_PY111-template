from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    l = 0
    r = len(arr) - 1

    while r - l > 2:
        m = (l + r) // 2
        if elem > arr[m]:
            l = m + m % 2
        else:
            r = m - m % 2 + 1

    if elem == arr[l]:
        return l
    if elem == arr[r]:
        return r
    else:
        return None
