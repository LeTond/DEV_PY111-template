"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any
import numpy as np

q = np.array([], dtype=int)


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global q

    for minimum in range(0, 11):
        if minimum == priority:
            q = np.concatenate([q, [elem]])

    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global q

    if q.size > 0:
        x = q[0]
        q = np.delete(q, 0)

        return x
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global q

    try:
        for minimum in range(0, 11):
            if minimum == priority:
                top = q[ind]

                return top

    except IndexError:
        print("IndexError")


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global q

    q = np.array([], dtype=int)

    return None


if __name__ == "__main__":
    dequeue()
