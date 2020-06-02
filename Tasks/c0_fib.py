def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        if n > 999 or n < 0:
            raise ValueError("ValueError")
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    fib1 = 1
    fib2 = 1
    count = 2
    if n > 999 or n < 3:
        raise ValueError("ValueError")
    while n > count:
        fib_sum = fib2 + fib1
        fib1, fib2 = fib2, fib_sum
        count += 1
    return fib_sum
