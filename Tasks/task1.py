

import numpy as np

array = np.random.randint(-100, 100, 40)

def liniar_search(array):
    minimum = min(array)
    for i, j in enumerate(array):
        if array[i] == minimum:
            print(array)
            print(f"Индекс минимального числа: {i}, Минимальное число: {j}")
            return i

liniar_search(array)
