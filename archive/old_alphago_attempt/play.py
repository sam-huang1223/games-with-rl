'''

Value network - Conv Net
Input: State
Output: Termination outcome

To generate training examples:
    Policy network - Conv net
    Input: State
    Output: Move

    To generate training examples
        Alpha-beta-pruning expert games
        * Run thousands of games with ABP
        against ABP (playing against itself)
        * Extract (state, move, outcome)
        for each player, then make
        player-agnostic

    Simulation function:
    Input: state, policy network
    Output: termination outcome
        Policy network against policy network

'''

from keras.models import load_model

model = load_model('./model.h5')
