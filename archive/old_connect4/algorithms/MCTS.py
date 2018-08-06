import numpy as np

from random import choice
from copy import deepcopy
import Connect4

## TODO look into visualizing MCTS next moves from root node
## MCTS stats converges to minimax game tree values as more simulations are run
# https://www.youtube.com/watch?v=Fbs4lnGLS8M

class Node():
    def __init__(self, name, state, parent, total_score, n_sims):
        self.name = name
        self.parent = parent
        self.children = []
        self.state = state
        self.total_score = total_score
        # sum of all scores along all paths from leaf nodes
        self.n_sims = n_sims
        # number of simulations conducted along any path to the root

class search():
    def __init__(self, state, epochs):
        self.epochs = epochs
        self.game = Connect4

        self.states = {}
        self.human = 1
        self.ai = -1
        self.root = Node(name='Layer 0',state=state, parent=None, total_score=0, n_sims=0)

        self.count = 0
        while True:
            self.count += 1
            self.path = []
            can_stop, value = self.tree_search(node=self.root, depth=1)
            #print('Epoch {epoch} - Value = {value}'.format(epoch=self.count, value=value))
            if can_stop and self.count >= self.epochs:
                break

        print('{name}\t\t\t\tparent: {parent}\t\t#children: {num_children}\ttotal score: {total_score}\t\t#simulations: {n_sims}'.format(
                name=self.root.name, parent=None, num_children=len(self.root.children),
                total_score=self.root.total_score, n_sims=self.root.n_sims))
        for node in self.root.children:
            print('{name}\tparent: {parent}\t\t#children: {num_children}\ttotal score: {total_score}\t\t#simulations: {n_sims}'.format(
                  name=node.name, parent=node.parent.name, num_children=len(node.children), total_score=node.total_score,
                  n_sims=node.n_sims))

        UCB_next_moves = []
        for child in self.root.children:
            UCB_next_moves.append(self.UCB(action_mean=child.total_score / child.n_sims,
                                           total_sims=self.root.n_sims, action_sims=child.n_sims))
        self.optimal_next_move = np.argmax(np.array(UCB_next_moves))

    def tree_search(self, node, depth):
        # TODO add comments as I go
        moves = self.game.generate_moves(node.state)
        moves_UCB = []
        for move in moves:
            player = self.human if depth % 2 == 0 else self.ai
            node, next_node = self.expand_one_node(node, move, depth, player)
            if next_node.n_sims == 0:
                moves_UCB.append(1e9)
            else:
                moves_UCB.append(self.UCB(action_mean=next_node.total_score/next_node.n_sims,
                                          total_sims=self.root.n_sims+1, action_sims=next_node.n_sims))

        duplicates_dict = {token: [index for index in range(len(moves_UCB)) if moves_UCB[index] == token]
                           for token in set(moves_UCB)}
        max_UCB = max(moves_UCB)

        if len(duplicates_dict[max_UCB]) > 1:
            can_stop = False

            for idx in duplicates_dict[max_UCB]:
                value = self.simulate(node.children[moves[idx]])
                self.backpropagate(node.children[moves[idx]], value)
                return can_stop, value
        else:
            can_stop = True
            best_UCB_move = np.argmax(np.array(moves_UCB))
            next_node = node.children[moves[best_UCB_move]]
            if next_node.n_sims == 0:
                value = self.simulate(next_node)
                self.backpropagate(next_node, value)
                return can_stop, value
            else:
                self.path.append(best_UCB_move)
                return self.tree_search(node=next_node, depth=depth + 1)

    def expand_one_node(self, node, move, depth, player):
        self.path.append(move)
        next_state = self.game.modify_state(deepcopy(node.state), move, player)
        if search.convert_to_string(self.path) in self.states:
            next_node = self.states[search.convert_to_string(self.path)]
        else:
            next_node = Node(name='Layer {depth} - Move {move}'.format(depth=depth, move=move),
                             state=next_state, parent=node, total_score=0, n_sims=0)
            node.children.append(next_node)
        self.states[search.convert_to_string(self.path)] = next_node
        self.path = self.path[:-1]
        return node, next_node

    def UCB(self, action_mean, total_sims, action_sims):
        return action_mean + 2*np.sqrt(np.log(total_sims)/action_sims)

    def simulate(self, node):
        # behave randomly while honoring constraints
        # 1 is win, -1 is loss
        simulation_state = deepcopy(node.state)
        while True:
            human_moves = self.game.generate_moves(simulation_state)
            if not human_moves:
                return 0
            human_move = choice(human_moves)
            simulation_state = self.game.modify_state(simulation_state, human_move, self.human)

            ai_moves = self.game.generate_moves(simulation_state)
            if not ai_moves:
                return 0
            ai_move = choice(ai_moves)
            simulation_state = self.game.modify_state(simulation_state, ai_move, self.ai)

            outcome = self.game.game_outcome(simulation_state, abs(self.ai))
            if outcome == -self.game.constant:
                return -1
            elif outcome == self.game.constant:
                return 1

    def backpropagate(self, node, value):
        node.total_score += value
        node.n_sims += 1
        if node.parent is not None:
            self.backpropagate(node.parent, value)

    @staticmethod
    def convert_to_list(path):
        return path.replace(" ", "").strip("['']").split("','")

    @staticmethod
    def convert_to_string(path):
        return str(path).replace("','", '->')


if __name__ == '__main__':
    epochs = 2000
    state = np.zeros((6, 7), dtype=int)
    algorithm = search(state, epochs)


