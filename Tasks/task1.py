import numpy as np

array = np.random.randint(-100, 100, 40)


def liniar_search(array):
    minimum = min(array)
    for i, j in enumerate(array):
        if array[i] == minimum:
            # print(array)
            print(f"Индекс минимального числа: {i}, Минимальное число: {j}")
            return i


liniar_search(array)

def equal(array):

    index_mini = 0
    for i in range(len(array)):
        if array[index_mini] >= array[i]:
            index_mini = i
            # print(array)
    print(f"Индекс минимального числа: {index_mini}, Минимальное число: {array[index_mini]}")
    return index_mini


print(equal(array))
