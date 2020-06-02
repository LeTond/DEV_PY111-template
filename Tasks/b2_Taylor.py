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
    n = 0
    step = (-1) ** n * x ** (2 * n + 1) / fact_sin(n)

    while abs(step) > 0.0001:
        sinx_x += step
        n += 1

    return sinx_x


def fact(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial


def fact_sin(n):
    factorial = 3
    while n > 1:
        factorial *= (2 * n + 1)
        n -= 1
    return factorial
