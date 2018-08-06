# keep good logs, visualize tree structure with pydotplus
import logging
logger = logging.getLogger(__name__)
from dataclasses import dataclass
from copy import deepcopy

from ..visualization.tree_display import Tree
from ..environments.TicTacToe import State, TicTacToe

@dataclass
class Node:
    state: State
    value: float = None
    children: list = None

class MinimaxAgent:
    def __init__(self):
        self.MAX_CONSTANT = 1e6
        #self.root = Node(value=5, children=[Node(3), Node(4)])
        #tree = Tree(self.root)
        
        env = TicTacToe()
        self.current_state = Node(state=deepcopy(env.state)) 

