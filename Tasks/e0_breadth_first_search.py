from typing import Hashable, List
import matplotlib.pyplot as plt
import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order
    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    list_ = list(g.neighbors(start_node))
    len_graph = g.number_of_nodes()
    list2 = [start_node]
    while len(list2) < len_graph:
        for i in range(len(list_) - 1):
            if list_[0] not in list2:
                list2.append(list_[0])
                list_ += list(g.neighbors(list_[0]))
            list_.remove(list_[0])
    # nx.draw(g, with_labels=True)
    # plt.show()
    return list2
