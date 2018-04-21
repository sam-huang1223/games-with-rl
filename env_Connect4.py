"""





"""

import numpy as np

class Node:
    """
    Board structure:
    Every node has up to 8 neighbors, indexed from 0-7 with 0 starting from the
    upper left corner then 1..7 moving clockwise
    """
    def __init__(self, neighbors, occupied=False, player=False):
        self.occupied = occupied
        self.player = player
        self.neighbors = neighbors

class Connect4:
    """

    """
    def __init__(self):
        self.HEIGHT = 6
        self.WIDTH = 7
        self.BOARD = np.ones((self.HEIGHT + 2, self.WIDTH + 2), dtype=np.bool)  # 6 rows, 7 columns
        self.BOARD[0, :], self.BOARD[-1,:], self.BOARD[:,0], self.BOARD[:,-1] = [False]*4
        # Board represented by connections stemming from
        # self.upper_left_corner (1,1) in self.BOARD, ends at (-2,-2) in self.BOARD

        self.upper_left_corner = Node(self._get_neighbors(1,1))
        self.reset_board()


    def heuristic_eval(self):
        raise NotImplementedError


    def step(self):
        pass


    def reset_board(self):
        self._propagate(self.upper_left_corner, x=1, y=1)

    def _propagate(self, node, x, y):
        pass


    def _get_neighbors(self, x, y):
        neighbors = np.zeros(8, dtype=np.bool)

        left_col = self.BOARD[:, x-1].any()
        right_col = self.BOARD[:, x+1].any()
        upper_row = self.BOARD[y-1, :].any()
        lower_row = self.BOARD[y+1, :].any()

        if upper_row:
            if left_col:
                neighbors[0] = True
            neighbors[1] = True
            if right_col:
                neighbors[2] = True

        if right_col:
            neighbors[3] = True

        if lower_row:
            if right_col:
                neighbors[4] = True
            neighbors[5] = True
            if left_col:
                neighbors[6] = True

        if left_col:
            neighbors[7] = True

        assert len(neighbors) == 8, "_get_neighbors does not return 8 neighbors"
        return neighbors

    def draw(self):
        pass


env = Connect4()
