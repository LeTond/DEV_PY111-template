from typing import Hashable, Mapping, Union
import networkx as nx
import matplotlib.pyplot as plt

list_ = []


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    diction = {}

    for i in g.nodes:
        diction[i] = float("inf")

    diction[starting_node] = 0
    len_g = len(list(g.edges))
    exit_ = True

    while exit_:
        exit_ = False
        for i in range(len_g):
            k = list(g.edges)[i][0]
            h = list(g.edges)[i][1]
            if g[k][h]["weight"] + diction[k] < diction[h]:
                diction[h] = g[k][h]["weight"] + diction[k]
                exit_ = True

    print(diction)
    # nx.draw(g, with_labels=True)
    # plt.show()

    return diction
