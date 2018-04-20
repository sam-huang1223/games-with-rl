"""
Q Learning implementation (the old-fashioned table-based way)

Converages to approximate basic strategy around timestep ___

Assumptions:
    1) If both possible actions have the same Q-value, choose to HIT
Resources:
    1) https://studywolf.wordpress.com/2012/11/25/reinforcement-learning-q-learning-and-exploration/
    2) https://pandas.pydata.org/pandas-docs/stable/10min.html
    *https://pandas.pydata.org/pandas-docs/stable/cookbook.html#cookbook
"""

import pandas as pd
import numpy as np


class QTable:
    """
    win rate: ~_% after 1m timesteps
    cash remaining (no bet size variation): _% after 1m timesteps (10m starting cash)
    cash remaining (bet size variation): _% after 1m timesteps (10m starting cash)

    win rate: ~43% after 100000 timesteps
    cash remaining: 86.4% after 100000 timesteps (1m starting cash)
    """
    def __init__(self, actions):
        self.actions = actions
        self.epsilon = 0.9  # could also scale by q-value -> higher q-value = lower likelihood of random exploration
        self.num_updates = 0

        indices = pd.MultiIndex.from_product(
            iterables=[range(2,12), range(12, 22)],
            names=['Dealer Card', 'Player Cards']
        )
        self.table = pd.DataFrame(
            data=np.zeros((len(indices),len(actions)), dtype=int),
            index=indices,
            columns=self.actions
        )

    def choose_action(self, dealer_value, player_value):
        if np.random.random() > self.epsilon:
            return np.random.choice(self.table.columns)
        else:
            best = max(self.table.loc[dealer_value, player_value])  # loc[i,j] selects the row at index1, index2
            if self.table.loc[dealer_value, player_value]['STAY'] == best:
                return "STAY"
            elif self.table.loc[dealer_value, player_value]['HIT'] == best:
                return "HIT"

    def update(self, action, dealer_card, player_value, reward):
        self.table.loc[dealer_card, player_value][action] += reward

        self.num_updates += 1
        if self.num_updates % 2000 == 0:
            self.epsilon += 0.01
        #if self.num_updates % 10000 == 0:
        #    self.table.to_csv("iteration {}".format(self.num_updates))

    # nothing is improving, stuck at 27% win rate, WHY???
    # 1 hr of scanning through code later, realized I was multiplying epsilon by 0.01 instead of by 1.01 to increase it by 1% every 1000 timesteps...


class QTableVaryBet:
    """
    Basic Strategy has higher win rate and regular QLearning is struggling to
    converge - can varying bet sizes help Q Learning beat basic strategy?
    """
    def __init__(self):
        pass

    def choose_action(self):
        pass

    def get_bet_size(self):
        pass

    def update(self):
        pass
