import numpy as np


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """

    chess_board_ = np.zeros(shape)
    M, N = chess_board_.shape
    chess_board_[0][0] = 1

    for j in range(0, M):
        for i in range(0, N):
            if chess_board_[j][i] != 0:
                try:
                    if j <= M - 3 and i <= N - 2:
                        chess_board_[j + 2][i + 1] += 2 * chess_board_[j][i]
                    if j <= M - 2 and i <= N - 3:
                        chess_board_[j + 1][i + 2] += 2 * chess_board_[j][i]
                    if i >= 2:
                        chess_board_[j + 1][i - 2] += 2 * chess_board_[j][i]
                    if i >= 1:
                        chess_board_[j + 2][i - 1] += 2 * chess_board_[j][i]
                except IndexError:
                    None

    print(chess_board_)
    return chess_board_[point[0]][point[1]]


def reverse_horse(point, shape, lvl, max_lvl):
    """
    Количество минимальных шагов, которыми можем прийти из клетки в клетку
    :param point:
    :param shape:
    :return: минимально количество шагов
    """
    x, y = point
    if point == (0, 0):
        return 0
    l = []
    if lvl > max_lvl:
        return 1005

    if y - 2 >= 0 and x - 1 >= 0:
        l.append(reverse_horse((x - 1, y - 2), shape, lvl+1, max_lvl))
    if y - 2 >= 0 and x + 1 < shape[0]:
        l.append(reverse_horse((x + 1, y - 2), shape, lvl+1, max_lvl))
    if y - 1 >= 0 and x + 2 < shape[0]:
        l.append(reverse_horse((x + 2, y - 1), shape, lvl+1, max_lvl))
    if y - 1 >= 0 and x - 2 >= 0:
        l.append(reverse_horse((x - 2, y - 1), shape, lvl+1, max_lvl))
    if l:
        return min(l) + 1
    else:
        return 1005

if __name__ == "__main__":
    # print(calculate_paths((17, 12), (16, 9)))
    print(reverse_horse((20, 20), (21, 21), 0, 16))
