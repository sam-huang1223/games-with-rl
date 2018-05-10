import pytest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# above code allows for imports from files in the parent directory

from env_Connect4 import Connect4, Node

def test_visualize_graph():
    ### outputs to output/test_graph_viz.png
    env = Connect4()
    env.upper_left_corner.neighbors = [Node(next(env.ids)) for _ in range(8)]
    env.upper_left_corner.neighbors[0].neighbors[0] = Node(next(env.ids))
    env.upper_left_corner.neighbors[0].neighbors[1] = Node(next(env.ids))
    env.upper_left_corner.neighbors[0].neighbors[1].neighbors[0] = Node(next(env.ids))
    env.upper_left_corner.neighbors[0].neighbors[5] = Node(next(env.ids))
    env.visualize_graph()


@pytest.mark.skip(reason="reset_board function incomplete due to unsolved challenge #1")
def test_reset_board():
    env = Connect4()  # can parameterize env once more game environments are complete
    env.reset_board()
    node = env.upper_left_corner
    print(node.neighbors)
    for _ in range(env.WIDTH):
        node = node.neighbors[3]
        print(node.neighbors)


@pytest.mark.skip(reason="visualize_board is incomplete")
def test_visualize_board():
    ### output/test_board_viz.png
    env = Connect4()
    env.visualize_board()
