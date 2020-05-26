"""
My little Stack
"""

from typing import Any

lis = []


def push(elem: int) -> None:
    """
    Operation that add element to stack
    :param elem: element to be pushed
    :return: Nothing
    """

    global lis
    lis.append(elem)
    return None


def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.
    :return: popped element
    """
    global lis
    # lis.append(15)

    if len(lis) >= 1:
        x = lis[len(lis) - 1]
        lis.remove(lis[len(lis) - 1])
        return x
    else:
        return None


def peek(ind: int = -1) -> Any:
    """
    Allow you to see at the element in the stack without popping it.
    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    global lis
    try:
        if lis[ind] is not None:
            print(lis[ind])
            top = lis[ind]
            return top
        elif lis[ind] is None:
            return None
    except IndexError:
        print("IndexError")
    return None


def clear() -> None:
    """
    Clear my stack
    :return: None
    """
    global lis
    lis = []

    return None


if __name__ == "__main__":
    print(pop())
