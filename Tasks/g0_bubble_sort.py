from typing import List

c = [2, 4, 6, 8, -10, 1, 2, 3, 0]


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    exit = True
    while exit:
        n = 0
        exit = False
        for i in range(1, len(container) - n):
            if container[i] < container[i - 1]:
                container[i], container[i - 1] = container[i - 1], container[i]
                n += 1
                exit = True
    return container


if __name__ == '__main__':
    print(sort(container=c))
