from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, l = 0, r = None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if r is None:
        r = len(arr) - 1
    if l > r:
        return None

    m = (l + r) // 2
    if elem == arr[m]:
        return m
    if elem < arr[m]:
        return binary_search(elem, arr, l, m-1)
    return binary_search(elem, arr, m+1, r)


if __name__=="__main__":
    print(binary_search(8, [1, 1, 2, 3, 4, 5, 6, 7, 10]))
    print(binary_search(5, [1, 1, 2, 3, 4, 5, 6, 7, 10]))
