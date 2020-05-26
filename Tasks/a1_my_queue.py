"""
My little Queue
"""
from typing import Any

q = []


def enqueue(elem: Any) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global q

    q.append(elem)
    print(elem)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if no elements.

    :return: dequeued element
    """
    global q

    if len(q) >= 1:
        x = q[0]
        q.remove(q[0])
        return x
    else:
        return None
    # if len(q) >= 1:
    #     return q.pop(0)
    # else:
    #     return None


def peek(ind: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global q

    try:
        if q[ind] is None:
            return None
        else:
            print(q[ind])
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

    q = []

    return None


if __name__ == "__main__":
    peek(2)
    print(dequeue())
    print([i for i in range(10)])
