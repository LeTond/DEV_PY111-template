"""
Вычисление сложности
"""


def o_notation(arr=[1, 2, 3, 4]):
    a = len(arr) - 1  # 1 + 1
    out = list()  # 1
    while a > 0:  # log1.7(N)
        out.append(arr[a])  # N
        a = a // 1.7  # 1
    out.merge_sort()  # Nlog(N)


## 2 + 1 + log1.7(N) * (1+N) +NlogN = 3 + Nlog1.7(N) + Nlog(N) = Nlog(N)


"""
Считалка
"""

import collections


def funct(K=3):
    n_list = [1, 2, 3, 4, 5, 6, 333, 20]
    deqeue_ = collections.deque(enumerate(n_list))
    while len(deqeue_) > 1:
        deqeue_.rotate(-K)
        deqeue_.pop()
    print(f"Номер последнего оставшегося: {deqeue_[0][0] + 1}\n"
          f"Последний оставшийся: {deqeue_[0][1]}")


"""
Конь
"""

import numpy as np
import matplotlib.pyplot as plt

# import networkx as nx


shape = (5, 7)
chess_board_ = np.random.randint(1, 10, (shape))
print(chess_board_)


def calculate_paths(chess_board_):
    g = nx.Graph()
    M, N = chess_board_.shape
    for i in range(N):
        for j in range(M):
            g.add_node((j, i))
            if j - 1 > 0:
                g.add_weighted_edges_from([((j, i), (j - 1, i), chess_board_[j - 1, i])])
            if i - 1 > 0:
                g.add_weighted_edges_from([((j, i), (j, i - 1), chess_board_[j, i - 1])])
            if j + 1 < M and i <= N:
                g.add_weighted_edges_from([((j, i), (j + 1, i), chess_board_[j + 1, i])])
            if i + 1 < N and j <= M:
                g.add_weighted_edges_from([((j, i), (j, i + 1), chess_board_[j, i + 1])])

    pos = nx.spring_layout(gf)
    nx.draw(g, pos, with_labels=True)
    labels = {e: g.edges[e] for e in g.edges}
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, with_labels=True)
    plt.show()
    dijkstra(g, stX=1, stY=1, X=3, Y=6)
    return g


def dijkstra(g, stX, stY, X, Y):
    diction = {}
    starting_node = (stX, stY)
    for i in g.nodes:
        diction[i] = float("inf")

    diction[starting_node] = 0
    len_g = len(list(g.edges))
    exit_ = True

    while exit_:
        exit_ = False
        for i in range(len_g):
            k = list(g.edges)[i][0]  # from "A"
            h = list(g.edges)[i][1]  # to "B"
            if g[k][h]["weight"] + diction[k] < diction[h]:
                diction[h] = g[k][h]["weight"] + diction[k]
                exit_ = True
    print(f"Минимальная стоимость пути до точки {X, Y}: {diction[(X, Y)]}")
    return diction


"""
Посчитать число компонент свзности графа
"""

import networkx as nx

counter = 0
list2 = []
graph = nx.Graph()
graph.add_nodes_from("ABCDEFGHIJ")
graph.add_edges_from([
    ('B', 'G'),
    ('F', 'G'),
    ('G', 'C'),
    ('G', 'H'),
    ('G', 'I'),
    ('C', 'H'),
    ('I', 'H'),
    ('H', 'J'),
    ('E', 'D'),
])
len_graph = graph.number_of_nodes()


def freedom(start_node, list2, g=graph):
    list_ = list(g.neighbors(start_node))
    if len(list_) == 0:
        list2.append(start_node)
    else:
        while list_ != []:
            if len(list_) > 0:
                if list_[0] not in list2:
                    list2.append(list_[0])
                    list_ += list(g.neighbors(list_[0]))
                list_.remove(list_[0])


def componenti_svyaznosti(counter):
    i = 0
    while len(list2) < len_graph:
        start_node = list(graph.nodes)[i]
        if start_node not in list2:
            freedom(start_node, list2, graph)
            counter += 1
        else:
            i += 1
    print(f" Число компонент связности: {counter}")


"""
Консенсус строка
"""

from collections import Counter

list_ = ['BTTA',
         'AGTD',
         'AGCD',
         'AGAD']


def consensus(list_):
    dot = []
    answer = ""
    counter = 0
    len_cons = len(list_[0])
    enter = ""
    while len(answer) < len_cons:
        for i in range(len(list_)):
            enter += list_[i]
            print(enter)
        for j in range(counter, len(enter), 4):
            dot.append(enter[j])
        counter += 1
        answer += Counter(dot).most_common(1)[0][0]
    print(f"Консенсус - строка: {answer}")


"""
Аренда ракет
"""


def rocket_money():
    zayavki_na_arendu = ((0, 3), (6, 8), (10, 15), (15, 20), (20, 21), (21, 23), (20, 23))
    spisok2 = [0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in zayavki_na_arendu:
        sp = (spisok2[j] for j in range(i[0] + 1, i[1] + 1))
        if None in sp:
            print(f"Этот интервал невозможно забронировать: {i[0], i[1]}")
        else:
            for k in range(i[0], i[1] + 1):
                spisok2[k] = None
    print(list(enumerate(spisok2)))


"""
Сортировка
"""
from collections import defaultdict
import random

array = [random.randint(13, 25) for i in range(10 ** 4)]


def CountingSort(array, mn, mx):
    count = defaultdict(int)

    for i in array:
        count[i] += 1

    result = []

    for j in range(mn, mx + 1):
        result += [j] * count[j]

    return result


if __name__ == '__main__':
    # funct()
    print(calculate_paths(chess_board_))
    # consensus(list_)
    # componenti_svyaznosti(counter)
    # rocket_money()
    # print(CountingSort(array, 13, 25))
