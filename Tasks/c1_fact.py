def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """



    if n == 1:
        return 1
    else:
        if n > 900 or n <= 0:
            raise ValueError("ошибка")
        return n * factorial_recursive(n-1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    count = 1

    for i in range(1, n+1):
        count *= i


    print(n)
    return count

# print(factorial_recursive(99))