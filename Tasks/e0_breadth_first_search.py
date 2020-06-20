from typing import Hashable, List
import matplotlib.pyplot as plt
import networkx as nx

list_ = []


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    g2 = nx.Graph()
    g2.add_node(start_node)
    list_ = list(g.neighbors(start_node))

    while len(list(g2.nodes)) < len(list(g.nodes)):
        for i in range(len(list_) - 1):
            if list_[i] != list(g2.nodes)[0]:
                g2.add_node(list_[0])
                list_ += list(g.neighbors(list_[0]))
            list_.remove(list_[0])
    # nx.draw(g, with_labels=True)
    # plt.show()
    return list(g2.nodes)
