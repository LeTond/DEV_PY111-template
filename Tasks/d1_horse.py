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
    cicle = 0
    while n < M:
        for j in range(0, M-2):
            for i in range(0, N-1):
                try:
                    if chess_board_[j][i] != 0:
                        chess_board_[j + 2][i + 1] = 2 * chess_board_[j][i]
                        chess_board_[j + 1][i + 2] = 2 * chess_board_[j][i]
                        if i >= 2:
                            chess_board_[j + 1][i - 2] = 2 * chess_board_[j][i]
                        if i >= 1:
                            chess_board_[j + 2][i - 1] = 2 * chess_board_[j][i]

                    if chess_board_[point[0]][point[1]] > 0:
                        counter += chess_board_[point[0]][point[1]]
                        cicle += 1
                        chess_board_[point[0]][point[1]] = 0
                except IndexError:
                    None

        n += 1
    print(cicle)
    return counter

if __name__ == "__main__":
    print(calculate_paths((8, 8), (7, 7)))
