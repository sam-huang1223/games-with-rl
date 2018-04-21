"""





"""

import numpy as np

class Node:
    """
    Board structure:
    Every node has up to 8 neighbors, indexed from 0-7 with 0 starting from the
    upper left corner then 1..7 moving clockwise
    """
    def __init__(self, occupied=False, player=False):
        self.occupied = occupied
        self.player = player
        self.neighbors = [None]*8

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

        self.upper_left_corner = Node()
        self.reset_board()

        node = self.upper_left_corner

        #test
        print(node.neighbors)
        for _ in range(self.WIDTH):
            node = node.neighbors[3]
            print(node.neighbors)


    def heuristic_eval(self):
        raise NotImplementedError


    def step(self):
        pass


    def reset_board(self):
        self._propagate(self.upper_left_corner, x=1, y=1)

    def _propagate(self, node, x, y):  # if 2 functions have the same inputs, they can likely be merged
        def _recurse(node, neighbor, x, y):
            if not node.neighbors[neighbor]:
                node.neighbors[neighbor] = Node()
                self._propagate(node.neighbors[neighbor], x, y)

        def _check_neighbor():
            pass

        if x < 0 or x > self.WIDTH or y < 0 or y > self.HEIGHT:
            return

        left_col = self.BOARD[:, x-1].any()
        right_col = self.BOARD[:, x+1].any()
        upper_row = self.BOARD[y-1, :].any()
        lower_row = self.BOARD[y+1, :].any()

        if upper_row:
            if left_col:
                if not _check_neighbor():
                    if not _check_neighbor():
                        _recurse(node, 0, x - 1, y - 1)
            _recurse(node, 1, x, y - 1)
            if right_col:
                _recurse(node, 2, x + 1, y - 1)

        if right_col:
            _recurse(node, 3, x + 1, y)

        if lower_row:
            if right_col:
                _recurse(node, 4, x + 1, y + 1)
            _recurse(node, 5, x, y + 1)
            if left_col:
                _recurse(node, 6, x - 1, y + 1)

        if left_col:
            _recurse(node, 7, x - 1, y)

    def draw(self):
        pass


env = Connect4()
