from dataclasses import dataclass

import numpy as np

@dataclass
class State:  # True represents player, False represents AI
    state: np.array
    turn: bool

class TicTacToe:
    def __init__(self):
        self.state = State(np.empty(shape=(3,3), dtype=object), True)

TicTacToe()
    