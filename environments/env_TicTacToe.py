import numpy as np
from visualization.graph_visualizer import draw_graph
from visualization.board_visualizer import DrawBoard

class Node:
    """
    Board structure:
    Every node has up to 8 neighbors, indexed from 0-7 with 0 starting from the
    upper left corner then 1..7 moving clockwise
    """
    def __init__(self, id, x=None, y=None, occupied=False, player=False):
        self.id = id
        self.x = x
        self.y = y
        self.occupied = occupied
        self.player = player

        self.neighbors = np.empty(8, dtype=object)
        self.score = [0]*3  # -1 if win is not possible in that direction

    def __repr__(self):
        return "Node {id} at ({x},{y})".format(id=self.id, x=self.x, y=self.y)


class TicTacToe:
    def __init__(self):
        self.HEIGHT = 3
        self.WIDTH = 3
        self.NEIGHBORS_X_DELTA = [-1, 0, 1, 1, 1, 0, -1, -1]  # x-coordinate delta from center node for neighbor [INDEX]
        self.NEIGHBORS_Y_DELTA = [-1, -1, -1, 0, 1, 1, 1, 0]  # y-coordinate delta from center node for neighbor [INDEX]
        self.BOARD = np.empty((self.HEIGHT, self.WIDTH), dtype=object)

        self.ids = self._id_generator()

        self.BOARD_UPPER_LEFT_CORNER = Node(next(self.ids), x=0, y=0)
        self.BOARD[0][0]= self.BOARD_UPPER_LEFT_CORNER

    def _id_generator(self):
        for i in range(1, self.WIDTH*self.HEIGHT + 1):  # 1 id for each node
            yield i

    def reward_eval(self):
        """Only used by RL algorithms that require non-binary reward functions"""
        raise NotImplementedError

    def step(self, player_move):
        raise NotImplementedError
        # update board based on player move
        # get optimal move from AI
        # update board based on AI move -> get new state, moves available
        # calculate reward
        # determine end
        # return state, moves available, reward, end

    def reset_board(self):
        self._propagate(self.BOARD_UPPER_LEFT_CORNER)

    def _propagate(self, node):
        for idx, neighbor, x_delta, y_delta in zip(range(len(node.neighbors)), node.neighbors,
                                                   self.NEIGHBORS_X_DELTA, self.NEIGHBORS_Y_DELTA):
            if not neighbor:
                new_x = node.x+x_delta
                new_y = node.y+y_delta
                if 0 <= new_x < self.WIDTH and 0 <= new_y < self.HEIGHT:
                    if self.BOARD[new_y][new_x]:
                        node.neighbors[idx] = self.BOARD[new_y][new_x]
                    else:
                        node.neighbors[idx] = Node(id=next(self.ids), x=new_x, y=new_y)
                        self.BOARD[new_y][new_x] = node.neighbors[idx]
                        self._propagate(self.BOARD[new_y][new_x])

    def visualize_graph(self, output_path='output/test_tictactoe_graph_viz.png'):  # ensure filename ends with .png
        draw_graph(root=self.BOARD_UPPER_LEFT_CORNER, node_obj_representation=Node, output_path=output_path)

    def visualize_board(self, output_path="../output/test_tictactoe_board_viz.html"):
        """ Created to visualize the state of a game board via a charting tool (e.g. bokeh) """
        parameters = {'width': self.WIDTH, 'height': self.HEIGHT, 'board': self.BOARD,
                      'output_path':output_path}
        DrawBoard(params=parameters)


if __name__ == '__main__':
    env = TicTacToe()
    env.reset_board()
    env.BOARD[2,2].occupied = True
    env.BOARD[0,2].occupied = True
    env.BOARD[1,1].occupied = True
    env.BOARD[1,1].player = True

    print(env.BOARD)
    env.visualize_board()
