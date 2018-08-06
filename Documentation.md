# src.algorithms.optimal_agent.py

#### Design decision #1: associate every node with a seperate copy of its would-be state and estimated  value

1) easier to visualize changes moving down different branches of the tree -> easier to debug
2) removes need to rebuild tree every time -> improves runtime significantly
    
    next call of minimax can continue from the state associated with a node from the tree built by the previous call of minimax

must use deepcopy to avoid passing by reference in associating states with nodes - testing code below

    env = TicTacToe()
    self.current_state = Node(state=env.state) 
    logger.info(self.current_state)
    env.state.state[0][0] = 5
    logger.info(self.current_state) 
