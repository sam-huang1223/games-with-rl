class BasicStrategy:
    """
    win rate: ~44.6% after 1m timesteps
    cash remaining (no doubling): 89.9% after 1m timesteps (10m starting cash)
    cash remaining (doubling): 90.5% after 1m timesteps (10m starting cash)
    """
    def __init__(self):
        self.table = {
            2: [12],
            3: [12],
            4:[],
            5:[],
            6:[],
            7:[12,13,14,15,16],
            8:[12,13,14,15,16],
            9:[12,13,14,15,16],
            10:[12,13,14,15,16],
            11:[12,13,14,15,16]
        }

        self.doubling_table = {
            2: [10, 11],
            3: [9,10,11],
            4: [9,10,11],
            5: [9,10,11],
            6: [9,10,11],
            7: [10,11],
            8: [10,11],
            9: [10,11],
            10: [11],
            11: [11]
        }

    def choose_action(self, dealer_value, player_value):
        if player_value in self.table[dealer_value]:
            return 'HIT'
        return 'STAY'


    def get_bet_size(self, dealer_card, player_value, bet_size):
        if player_value in self.doubling_table[dealer_card]:
            return bet_size * 2
        return bet_size


