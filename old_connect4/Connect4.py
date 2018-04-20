import numpy as np

from collections import Counter
from copy import deepcopy

from algorithms import MCTS, Alpha_Beta_Pruning

# TODO look into visualizing connect4 board

# TODO Memoize evaluation function (check end, check vector, etc)
''' User input: Specify which algorithm to use '''

def get_type(x):
    return 'MAX' if x == 1 else 'MIN'

constant = int(10e9)

def generate_moves(state):
    '''return list of possible moves'''
    return [idx for idx in range(7) if state[0][idx] == 0]


def modify_state(state, move, player):
    '''updates a state with a given move'''
    state[np.where(state[:,move]==0)[0][-1]][move] = player
    return state

def game_outcome(state, player):
    '''returns the value of a state'''
    result = set([0])
    for row in state:
        if check_plausibility(row):
            result.add(check_end(indices_of_duplicates(row, player), player))
    for column in state.transpose():
        if check_plausibility(column):
            result.add(check_end(indices_of_duplicates(column, player), player))
    for diagonal in get_diagonals(state):
        if check_plausibility(diagonal):
            result.add(check_end(indices_of_duplicates(diagonal, player), player))

    return max(min(result), max(result), key=abs)

def check_plausibility(arr):
    '''checks if array can possibly contain a win'''
    count = Counter(arr)
    if count[-1] >= 4 or count[1] >= 4:
        return True
    else:
        return False

def check_end(dict, player, counter=1, level=1):
    '''checks whether either player won'''
    if level > 2:
        return 0
    for i in range(len(dict[player]) - 1):
        if dict[player][i+1] == dict[player][i] + 1:
            counter += 1
        else:
            counter = 1
        if counter == 4:
            return -player*constant
    return check_end(dict,-player,level=level+1)

def indices_of_duplicates(state, player):
    '''returns dictionary with keys as possible values and values as lists of indices'''
    return {token: [index for index in range(len(state)) if state[index] == token] for token in [0, player, -player]}

def get_diagonals(state):
    '''get all diagonals of length >= 4'''
    diagonals = [state[::-1, :].diagonal(i) for i in range(-state.shape[0] + 4, state.shape[1] - 3)]
    diagonals.extend(state.diagonal(i) for i in range(state.shape[1] - 4, -state.shape[0] + 3, -1))
    return [element.tolist() for element in diagonals]

class Connect4:
    def __init__(self, board):
        self.human = 1
        self.ai = -1
        self.nodes = []
        self.edges = []
        self.node_num = 0
        self.path_taken = []
        self.outcomes = {}

        self.search_depth = 4
        self.state = board
        self.construct_graph(self.state, self.ai, '0 MAX0-0')

    def construct_graph(self, starting_state, player, starting_node_name):
        self.path_taken.append(starting_node_name)
        if starting_node_name[starting_node_name.find(' ') + 1: starting_node_name.find(' ') + 4] == 'MAX':
            type = 1
        else:
            type = -1
        self.node_num += 1
        self.nodes.append([starting_node_name, get_type(type)])
        moves = generate_moves(starting_state)

        depth = int(starting_node_name[starting_node_name.find('-') - 1:starting_node_name.find('-')])
        outcome = self.evaluate(starting_state, self.ai, moves == [])
        if (depth + 1) > self.search_depth or moves == [] or abs(outcome) == constant:
            self.path_taken.append(outcome)
            self.outcomes[str(self.path_taken)] = starting_state
            self.edges.append([starting_node_name, outcome])
            self.path_taken = self.path_taken[:-2]
            return
        for move in moves:
            potential_state = deepcopy(starting_state)
            potential_state = modify_state(potential_state, move, player)
            potential_node_name = str(self.node_num) + ' ' + get_type(-type) + str(int(starting_node_name[starting_node_name.find('-') - 1:starting_node_name.find('-')]) + 1) + '-' + str(move)
            self.edges.append([starting_node_name, potential_node_name])
            self.construct_graph(potential_state, -player, potential_node_name)
        self.path_taken = self.path_taken[:-1]

    def evaluate(self, state, player, end):
        '''returns the value of a state'''
        score = 0
        result = set()
        for row in state:
            score += self.estimate_value(row, player)
            if check_plausibility(row):
                result.add(check_end(indices_of_duplicates(row, self.human), self.human))
        for column in state.transpose():
            score += self.estimate_value(column, player)
            if check_plausibility(column):
                result.add(check_end(indices_of_duplicates(column, self.human), self.human))
        for diagonal in get_diagonals(state):
            score += self.estimate_value(diagonal, player)
            if check_plausibility(diagonal):
                result.add(check_end(indices_of_duplicates(diagonal, self.human), self.human))

        if (constant in result) or (-constant in result) or (len(result) > 0 and end):
            return max(min(result),max(result),key=abs)
        else:
            return score

    def estimate_value(self, array, player):
        value = 0
        exp, count, tokens = (1, 1, 1)
        pieces = [i for i in range(len(array)) if array[i] == player]

        for token in pieces:
            if (len(array) - 1) - token > 2:
                for pos in range(token, len(array) - 1):
                    tokens += 1
                    if array[pos + 1] == 0:
                        count += 1
                    elif array[pos + 1] == player:
                        count += 1
                        exp += 2
                    else:
                        break
                    if tokens == 4:
                        value += count ** exp
                        break
            count, tokens, exp = (1, 1, 1)
            if token > 2:
                for pos in range(token, 0, -1):
                    tokens += 1
                    if array[pos - 1] == 0:
                        count += 1
                    elif array[pos - 1] == player:
                        count += 1
                        exp += 2
                    else:
                        break
                    if tokens == 4:
                        value += count ** exp
                        break
        return value

def notuglyprint(state):
    mapping = {0: '-', -1: 'O', 1: 'X'}
    return np.array([[mapping[char] for char in line] for line in state])

def play(algo_selection):
    game = Connect4(board=np.zeros((6,7), dtype=int))
    print(notuglyprint(game.state))

    while True:
        human_move_values = []
        ai_move_values = []
        possible_human_moves = generate_moves(game.state)
        try:
            human_move = int(input('Please enter your next move (0-6): '))
        except ValueError:
            print('Invalid move. Please enter another move')
            continue
        if human_move == -1:
            print('Thank you for playing!')
            break
        elif possible_human_moves == []:
            print('TIE')
            break
        elif human_move not in possible_human_moves:
            print('Invalid move. Please enter another move')
            continue
        game.state = modify_state(game.state, human_move, game.human)

        print(notuglyprint(game.state))

        if game.evaluate(game.state, game.human, generate_moves(game.state) == 0) == -constant:
            print('HUMAN WON')
            break

        if algo_selection == 'alpha beta pruning':
            game = Connect4(board=game.state)
            algorithm = Alpha_Beta_Pruning.Minimax([game.nodes, game.edges], False)
            ai_move = int(algorithm.path[1][-1])
        elif algo_selection == 'MCTS':
            epochs = 1000
            algorithm = MCTS.search(game.state, epochs)
            ai_move = algorithm.optimal_next_move

        print('AI move:', ai_move)
        game.state = modify_state(game.state, ai_move, game.ai)
        print(notuglyprint(game.state))

        if game.evaluate(game.state, game.ai, generate_moves(game.state) == 0) == constant:
            print('AI WON')
            break

        human_move_value = game.evaluate(game.state, game.human, possible_human_moves == [])
        human_move_values.append(human_move_value)
        print('Human value:', human_move_value)

        ai_move_value = game.evaluate(game.state, game.ai, generate_moves(game.state) == 0)
        ai_move_values.append(ai_move_value)
        print('AI value:', ai_move_value)
        ai_win_prob = ai_move_value / (ai_move_value + human_move_value)
        print('AI probability of winnning:', ai_win_prob)