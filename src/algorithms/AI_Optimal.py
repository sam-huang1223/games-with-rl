#inp = [[['A', 'MIN'], ['B', 'MAX'], ['C', 'MAX'], ['D', 'MAX'], ['E', 'MAX'], ['F', 'MIN'], ['G', 'MIN'], ['H', 'MIN'], ['I', 'MIN'], ['J', 'MIN'], ['K', 'MIN'], ['L', 'MIN'], ['M', 'MIN'], ['N', 'MIN'], ['O', 'MIN']], [['A', 'B'], ['A', 'C'], ['A', 'D'], ['A', 'E'], ['B', 'F'], ['B', 'G'], ['B', 'H'], ['C', 'I'], ['C', 'J'], ['D', 'K'], ['D', 'L'], ['E', 'M'], ['E', 'N'], ['E', 'O'], ['F', '6'], ['F', '3'], ['F', '2'], ['G', '5'], ['G', '9'], ['H', '4'], ['H', '1'], ['I', '6'], ['J', '6'], ['J', '12'], ['K', '13'], ['K', '14'], ['L', '6'], ['L', '12'], ['M', '2'], ['M', '5'], ['M', '7'], ['N', '6'], ['N', '7'], ['O', '12'], ['O', '2']]]

"""
Minimax Search with Alpha Beta Pruning allows for optimal play

The input consist of a graph represented as a list of lists of nodes and edges
    The list of nodes is a list of lists in the form of [NODE_NAME, 'MAX'/'MIN']
    The list of edges is a list of lists in the form of [START_NODE_NAME, END_NODE_NAME]
"""

# 1. Generate nodes
# 2. Run algorithm, only create new nodes if not found in generated nodes

from copy import deepcopy

constant = 100000


class Node:
    def __init__(self, index, children, type, alpha=-constant, beta=constant):
        self.index = index
        self.alpha = alpha
        self.beta = beta
        self.type = type
        self.children = children


class Minimax:
    def __init__(self, root, win_eval):
        self.NUM_NEIGHBORS = len(root.available_actions)
        self.win_eval = win_eval
        self.traversed = 0

        self.root = self._construct_tree(children=root.available_actions, idx=root.index[0], node_num=root.index[1])

        print(self.root.children[0].children[7].children[4].index)
        raise SystemError

        root_path = [self.root]

        if self.root.type == 'MAX':
            for child in self.root.children:
                child_score = self.alpha_beta_search(child, alpha=self.root.alpha, beta=self.root.beta)
                if child_score > self.root.alpha:
                    self.root.alpha = child_score
            self.game_value = self.root.alpha
        else:
            for child in self.root.children:
                child_score = self.alpha_beta_search(child, alpha=self.root.alpha, beta=self.root.beta)
                if child_score < self.root.beta:
                    self.root.beta = child_score
            self.game_value = self.root.beta
        print('The value of the game is:', self.game_value)

        self.path_to_root(self.root, root_path)

        self.minimax_path = []
        seen = set()
        for i in root_path:
            if i not in seen:
                self.minimax_path.append(i)
                seen.add(i)

        self.path = [i if isinstance(i, int) else i.index for i in self.minimax_path]
        print('Path: ', self.path)
        print('\nTraversed (count = {count}) '.format(count=self.traversed))

        if display:
            print('Final node values:')
            for element in sorted(self.print_tree(), key=lambda x: ord(x[5:x.find('type')].strip())):
                print(element)

    def _construct_tree(self, children, idx, node_num):
        root = Node(index=(idx, node_num), children=children, type="MIN" if idx % 2 == 0 else "MAX")
        root_children = deepcopy(root.children)


        for i in range(self.NUM_NEIGHBORS):
            if root.children[i]:
                child_children = deepcopy(root_children)
                child_children[i] = False
                root.children[i] = self._construct_tree(children=child_children, idx=idx+1, node_num=i+1)

        # build graph-based win evaluation (win_eval_func), if win state, connect to a leaf instead of a node

        return root


    def alpha_beta_search(self, node, alpha, beta):
        if isinstance(node, int):
            self.traversed += 1
            return node

        if node.type == 'MAX':
            node.beta = beta
            for child in node.children:
                a = self.alpha_beta_search(child, alpha=node.alpha, beta=node.beta)
                if a > node.alpha:
                    #print('node: {index} - alpha update:\tfrom {before} to {after}'.format(index=node.index, before=node.alpha, after=a))
                    node.alpha = a
                if node.alpha >= node.beta:
                    break
            return node.alpha

        else:
            node.alpha = alpha
            for child in node.children:
                b = self.alpha_beta_search(child, alpha=node.alpha, beta=node.beta)
                if b < node.beta:
                    #print('node: {index} - beta update:\tfrom {before} to {after}'.format(index=node.index, before=node.beta, after=b))
                    node.beta = b
                if node.beta <= node.alpha:
                    break
            return node.beta

    def path_to_root(self, node, root_path):
        if node.type == 'MAX':
            for child in node.children:
                if isinstance(child, int):
                    if child == node.alpha:
                        root_path.append(child)
                elif child.beta == node.alpha:
                    root_path.append(child)
                    self.path_to_root(child, root_path)
                    break
        else:
            for child in node.children:
                if isinstance(child, int):
                    if child == node.beta:
                        root_path.append(child)
                elif child.alpha == node.beta:
                    root_path.append(child)
                    self.path_to_root(child, root_path)
                    break
        return root_path

    def print_tree(self):
        return [('node: {index:<}\ttype: {type:<}\talpha: {alpha:<8}\tbeta: {beta:<8}\tchildren: {children}'.format(
                            index=node.index, type=node.type, alpha=node.alpha, beta=node.beta,
                            children=[child.index if not isinstance(child, int) else child for child in node.children]))
            for key, node in self.nodes.items()]


    #problem: specific sequence of moves (4 3 5 4 5 2 2 3 3 1 0 1) was causing poor gameplay
    #         issue was that search tree branching continued after making game-ending move,
    #         leading to weird behaviour using the minimax algorithm.
    #solution: I cut off the search tree whenever a move leads to a win

    #problem: algorithm not taking winning move because it did not find optimal path to leaf node matching game value.
    #         It found the first path that led to a winning leaf node, but not the shortest
    #solution: breadth-first search through the tree, until I hit a leaf node matching the game value

if __name__ == '__main__':
    class InputNode:
        def __init__(self, id, max=False):
            self.index = id
            self.max = max
            self.available_actions = [True, False, False, False, True, False, False, True, False]  # children in actual implementation

    class LeafNode:
        def __init__(self, value):
            self.value = value

    def win_eval_func():
        from environments.env_TicTacToe import TicTacToe
        env = TicTacToe()
        env.reset_board()
        env.BOARD[2, 2].player = -1
        env.BOARD[0, 2].player = -1
        env.BOARD[1, 1].player = 1

        env.print_board()

    win_eval_func()
    raise SystemError

    ####
    #_XO  123
    #O_O  456
    #X_X  789
    root = InputNode((0,1), max=False)  # 0th layer, 1st node

    # Value of the game graph=inp should be 5
    # Value of the game graph=root should be +1
    Minimax(root, win_eval_func)
