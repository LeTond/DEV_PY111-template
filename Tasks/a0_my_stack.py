"""
My little Stack
"""
from typing import Any

lis = [1, 3, 4, 4, 56, 7, 7, 4]

def push(elem: int) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """

    global lis
    lis.append(12)
    lis.clear()



def pop() -> Any:
    """
    Pop element from the top of the stack. If not elements - should return None.

    :return: popped element
    """
    global lis

    if len(lis) == 0:
        return None
    else:
        lis.pop(-1)


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the stack without popping it.

    :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
    :return: peeked element or None if no element in this place
    """
    global lis

    print(ind)
    return None


# Commit

def clear() -> None:
    """
    Clear my stack

    :return: None
    """


    return None


if __name__ == "__main__":
    push(0)
    print(pop())