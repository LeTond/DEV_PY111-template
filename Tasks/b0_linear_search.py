"""
This module implements some functions based on linear search algo
"""
import numpy as np
from typing import Sequence

array = np.random.randint(-100, 100, 40)


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    minimum = min(arr)
    for i, j in enumerate(arr):
        if arr[i] == minimum:
            print(f"Индекс минимального числа: {i}, Минимальное число: {j}")
            return i


def linear_search(array):
    minimum = min(array)
    for i, j in enumerate(array):
        if array[i] == minimum:
            # print(array)
            print(f"Индекс минимального числа: {i}, Минимальное число: {j}")
            return i


def equal(array):
    index_mini = 0
    for i in range(len(array)+1):
        if array[index_mini] >= array[i]:
            if i > len(array) or i < len(array):
                raise IndexError("IndexError")
            index_mini = i
        # print(array)
    print(f"Индекс минимального числа: {index_mini}, Минимальное число: {array[index_mini]}")
    return index_mini


if __name__ == "__main__":
    linear_search(array)
    print(equal(array))
