from typing import Hashable, Mapping, Union
import networkx as nx
import matplotlib.pyplot as plt

diction = {}
list_ = []

def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    print(g, starting_node)

    for i in g.nodes:
        diction[i] = float("inf")

    list_ = list(g.neighbors(starting_node))
    diction[list_[0]] = len(list(g.neighbors(starting_node)))

    while len(list_) < len(list(g.nodes)):
        for i in range(len(list(g.nodes)) - 1):
            for j in range(len(list(g.neighbors(list(g.nodes)[i]))) - 1):
                if list(g.neighbors(list(g.nodes)[i]))[j] != list_[-1]:
                    diction[list(g.nodes)[i]] += g[list(g.nodes)[i]][list(g.neighbors(list(g.nodes)[i]))[j]]["weight"]
                    list_ += list(g.neighbors(list(g.nodes)[i]))[j]

    print(g["B"]["E"]["weight"])
    print(list_)
    print(diction)
    # nx.draw(g, with_labels=True)
    # plt.show()

    return diction
