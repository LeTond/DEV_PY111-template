"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any
from collections import deque

q = deque()


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global q
    for minimum in range(len(q) + 1):
        if minimum == priority:
            q.append(elem)
            print(q)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    global q
    print(f"Длина списка: {len(q)}")
    if len(q) >= 1:
        x = q[0]
        q.remove(q[0])
        print(f"Возвращаемый начальный элемент списка: {x}")
        return x

    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global q
    for minimum in range(len(q) + 1):
        if minimum == priority:
            try:
                top = q[ind]
                print(f"Приоритет {priority}")
                print(f"Возвращение top: {top}")
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
