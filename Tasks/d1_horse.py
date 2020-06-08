import numpy as np


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    counter = 0
    chess_board_ = np.zeros(shape)
    M, N = chess_board_.shape
    chess_board_[0][0] = 1
    n = 1
    while n < M:
        for j in range(n - 1, M):
            for i in range(n - 1, N):
                if chess_board_[j][i] != 0:
                    if n - 1 < (j + 2) < M and 0 < (i + 1) < N:
                        chess_board_[j + 2][i + 1] = chess_board_[j][i] + 1
                        if M - 1 == j + 2 and N - 1 == i + 1:
                            counter += 2 ** (chess_board_[point[0]][point[1]] - 1)
                            chess_board_[point[0]][point[1]] = 0
                    if n - 1 < (j + 1) < M and 0 < (i + 2) < N:
                        chess_board_[j + 1][i + 2] = chess_board_[j][i] + 1
                        if M - 1 == j + 1 and N - 1 == i + 2:
                            counter += 2 ** (chess_board_[point[0]][point[1]] - 1)
                            chess_board_[point[0]][point[1]] = 0
                    if n - 1 < (j + 1) < M and 0 <= (i - 2) < N:
                        chess_board_[j + 1][i - 2] = chess_board_[j][i] + 1
                        if M - 1 == j + 1 and N - 1 == i - 2:
                            counter += 2 ** (chess_board_[point[0]][point[1]] - 1)
                            chess_board_[point[0]][point[1]] = 0
                    if n - 1 < (j + 2) < M and 0 <= (i - 1) < N:
                        chess_board_[j + 2][i - 1] = chess_board_[j][i] + 1
                        if M - 1 == j + 2 and N - 1 == i - 1:
                            counter += 2 ** (chess_board_[point[0]][point[1]] - 1)
                            chess_board_[point[0]][point[1]] = 0

        n += 1
    print(chess_board_)
    print("__________________")
    return counter


if __name__ == "__main__":
    print(calculate_paths((5, 5), (4, 4)))
