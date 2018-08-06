from src.environments import TicTacToe

def run():
    env = TicTacToe()
    env.reset_board()
    env.BOARD[2,2].player = -1
    env.BOARD[0,2].player = -1
    env.BOARD[1,1].player = 1

    print(env.BOARD)
    #env.visualize_graph()
    #env.visualize_board()

from src.algorithms.optimal_agent import MinimaxAgent

agent = MinimaxAgent()