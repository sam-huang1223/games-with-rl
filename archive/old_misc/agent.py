from env import BlackJack
from Q_learning import QTable
from Basic_Strategy import BasicStrategy


game = BlackJack()
brain = QTable(actions=game.actions)
#brain = BasicStrategy()

#TODO why the fk is the winrate at 41% instead of 43%???

#"""
INITIAL_CASH = 1000000
cash = 1000000
BET_SIZE = 10

count = 0
wins = 0
losses = 0

while count <= 100010:
    if count % 10000 == 10:
        print('Win ratio: ', wins/(wins + losses))
        print('% Cash remaining', (cash/INITIAL_CASH)*100)
        wins = 0
        losses = 0

    dealer_card = game.dealer_hand[1].number if isinstance(game.dealer_hand[1].number, int) else 10
    action = None
    player_value = game.player_value

    bet_size = BET_SIZE
    #bet_size = brain.get_bet_size(dealer_card, player_value, BET_SIZE)

    while not game.done:
        action = 'HIT'
        player_value = game.player_value
        if player_value > 11:
            action = brain.choose_action(dealer_card, player_value)
        game.step(action)

    if player_value <= 11:
        player_value += 10
    if action:
        brain.update(action, dealer_card, player_value, game.reward)

    if game.reward == -1:
        cash -= bet_size
        losses += 1
    elif game.reward == 1:
        wins += 1
        cash += bet_size

    game.reset()
    count += 1
#"""

"""
count = 0

while count <= 5:
    dealer_card = game.dealer_hand[1].number if isinstance(game.dealer_hand[1].number, int) else 10
    while not game.done:
        player_value = game.player_value
        for _ in range(game.player_aces):
            if player_value > 21:
                player_value -= 10
            else:
                break

        if player_value <= 11:
            action = 'HIT'
        else:
            action = brain.choose_action(dealer_card, player_value)
        print(action)
        print(game.step(action))

    if game.reward == -1:
        print('LOSE')
    elif game.reward == 1:
        print('WIN')

    game.reset()

    count += 1
"""
