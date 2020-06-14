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

    list2 = []
    list_ = list(g.neighbors(start_node))
    list2.append(start_node)

    while len(list_) > 0:

        if list_[0] in list2:
            list_.remove(list_[0])
        else:
            list2.append(list_[0])
            list_ = list(g.neighbors(list_[0])) + list_
            list_.remove(list_[0])
            for i in range(len(list_) - 1):
                if list_[0] in list2:
                    list_.remove(list_[0])
    return list2
