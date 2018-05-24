import pytest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# above code allows for imports from files in the parent directory

from environments.env_TicTacToe import TicTacToe, Node

# make use of setup functions

def test_visualize_graph():
    ### outputs to output/test_graph_viz.png
    env = TicTacToe()
    env.reset_board()
    env.visualize_graph(output_path='output/test_tictactoe_graph_viz.html')


def test_reset_board():
    env = TicTacToe()  # can parameterize env once more game environments are complete
    env.reset_board()
    assert sum(1 for e in env.BOARD_UPPER_LEFT_CORNER.neighbors[4].neighbors if e) == 8
    assert sum(1 for e in env.BOARD_UPPER_LEFT_CORNER.neighbors if e) == 3
    assert sum(1 for e in env.BOARD_UPPER_LEFT_CORNER.neighbors[4].neighbors[4].neighbors if e) == 3


def test_visualize_board():
    ### output/test_board_viz.png
    env = TicTacToe()
    env.reset_board()
    ## INCOMPLETE
    env.visualize_board(output_path='output/test_tictactoe_board_viz.html')
