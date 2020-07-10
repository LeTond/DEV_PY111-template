from typing import List


container = [23, 45, 1, -4, -566, 3, 45, 45, 23, 5, 7, 9, 5, 5, 5, 5, -4, -34, -55, 4, 56]


def recursion(container):

    if len(container) < 2:
        return container
    else:
        return merge(recursion(container[:len(container) // 2]), recursion(container[len(container) // 2:]))


def merge(con1, con2):
    ind1 = 0
    ind2 = 0
    res = []
    while ind1 < len(con1) and ind2 < len(con2):
        if con1[ind1] < con2[ind2]:
            res.append(con1[ind1])
            ind1 += 1
        else:
            res.append(con2[ind2])
            ind2 += 1
    if ind1 < len(con1):
        res += con1[ind1:]
    elif ind2 < len(con2):
        res += con2[ind2:]
    return res


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """


if __name__ == '__main__':
    print(recursion(container))
