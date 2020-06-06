"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

q = []


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global q

    for pr in range(11):
        if pr == priority:
            q.append([])
            q[pr].append(elem)
        else:
            q.append([])
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global q

    for pr in range(len(q)):
        if len(q[pr]) > 0:
            zero = q[pr][0]
            del q[pr][0]
            return zero
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global q

    try:
        for pr in range(11):
            if pr == priority:
                top = q[pr][ind]
                return top

    except IndexError:
        print("IndexError")


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global q

    q = []

    return None


if __name__ == "__main__":
    dequeue()
