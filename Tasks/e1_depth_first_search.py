from typing import Hashable, List
import networkx as nx
import matplotlib.pyplot as plt
from Tasks.a0_my_stack import *

list_ = []


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    g2 = nx.Graph()
    list_ = list(g.neighbors(start_node))
    g2.add_node(start_node)

    while len(list(g2.nodes)) < len(list(g.nodes)):
        if list_[0] in list(g2.nodes):
            list_.remove(list_[0])
        else:
            g2.add_node(list_[0])
            list_2 = list(g.neighbors(list_[0]))
            list_.remove(list_[0])
            for i in range(len(list_2) - 1):
                if list_2[0] in list(g2.nodes):
                    list_2.remove(list_2[0])
            list_ = list_2 + list_

    return list(g2.nodes)
