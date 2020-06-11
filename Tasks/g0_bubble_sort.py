from typing import List

c = [2, 4, 6, 8, -10, 1, 2, 3, 0]

def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    n = 0
    lenght = len(container)
    while n < lenght:
        for i in range(1, len(container)):
            if container[i] < container[i-1]:
                container[i], container[i-1] = container[i-1], container[i]
            elif container[i] == container[i-1]:
               pass
        n += 1
    return container


if __name__ == '__main__':
    print(sort(container=c))
