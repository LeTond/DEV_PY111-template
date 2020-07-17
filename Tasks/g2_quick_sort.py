from typing import List
import random
import sys

# sys.setrecursionlimit(10000)

container = [2, 4, 43, 5, 112, 9, 6, 8, -10, 1, 2, 3, 0]


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container
    else:
        mean = random.choice(container)
    container_left = [i for i in container if i < mean]
    container_mid = [i for i in container if i == mean]
    container_right = [i for i in container if i > mean]
    return sort(container_left) + container_mid + sort(container_right)


if __name__ == '__main__':
    print(sort(container))
