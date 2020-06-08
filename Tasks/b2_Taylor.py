"""
Taylor series
"""
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    result = 1
    n = 1
    step = x ** n / fact(n)

    while step > 0.0001:
        result += step
        n += 1
        step = x ** n / fact(n)
    return result


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sinx_x = x
    n = 1
    step = (-1) ** n * x ** (2 * n + 1) / fact(2 * n + 1)

    while abs(step) > 0.0001:
        sinx_x += step
        n += 1
        step = (-1) ** n * x ** (2 * n + 1) / fact(2 * n + 1)
    return sinx_x


def fact(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial


if __name__ == "__main__":
    print(sinx(3))
