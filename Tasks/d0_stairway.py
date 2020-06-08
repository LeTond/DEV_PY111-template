from typing import Union, Sequence

stairway = [1, 34, 1, 43, 1, 34, 2, 9]

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    cost = stairway.copy()
    cost2 = 0

    for i in range(2, len(stairway)):
        cost[i] = stairway[i] + min(cost[i-1], cost[i-2])
        cost2 = cost[i]
    return cost2


if __name__ == "__main__":
    print(stairway_path(stairway))
