from random import shuffle, seed

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __repr__(self):
        return "{number} of {suit}".format(number=self.number, suit=self.suit)

    def __add__(self, other):
        if isinstance(self.number, int):  c1=self.number
        else:                             c1=10
        if isinstance(other.number, int): c2=other.number
        else:                             c2=10
        return c1 + c2


class BlackJack:
    """
    Assumptions:
    1) Dealer hits until his hand sums to >= 17
    2) Player wins if player hand sums to 21 (even if dealer hand sums to 21), as long as player chooses to stay
    # 3) Do not hit on ace if "ace=11 total" is > 17 and > 10+dealer's face up card (this assumes dealer has a value 10 hidden card)

    Extentions: doubling up, splitting cards, extra "corner" bet
    """
    def __init__(self, seed_num=None):
        self.NUMBERS = [2,3,4,5,6,7,8,9,10,11,'J','Q','K']
        self.SUITES = ['D','C','H','S']
        self.cards = [Card(num, suit) for suit in self.SUITES for num in self.NUMBERS]
        self.actions = ['STAY', 'HIT']
        if seed_num:
            seed(seed_num)

        self.reset()

    def dealer_draw(self):
        self.dealer_hand.append(self.cards.pop(0))
        self.dealer_value += self.dealer_hand[-1].number if isinstance(self.dealer_hand[-1].number, int) else 10
        if self.dealer_hand[-1].number == 11:
            self.dealer_aces += 1

    def player_draw(self):
        self.player_hand.append(self.cards.pop(0))
        self.player_value += self.player_hand[-1].number if isinstance(self.player_hand[-1].number, int) else 10
        if self.player_hand[-1].number == 11:
            self.player_aces += 1

    def step(self, action):
        """ *Not returning available actions since they are static """
        if action == 'HIT':
            self.player_draw()
        elif action == 'STAY':
            self.done = True
            while self.dealer_value < 17:
                self.dealer_draw()

            if self.dealer_value - 10 * self.dealer_aces > 21:
                self.done = True
                self.reward = 1
                return self.state, self.done, self.reward

            for _ in range(self.player_aces):
                if self.player_value > 21:
                    self.player_value -= 10
                else:
                    break

            if self.player_value > self.dealer_value:
                self.reward = 1
            elif self.player_value < self.dealer_value:
                self.reward = -1

        if self.player_value > 21:
            self.done = True
            self.reward = -1

        return self.state, self.done, self.reward

    def reset(self):
        self.cards = [Card(num, suit) for suit in self.SUITES for num in self.NUMBERS]
        shuffle(self.cards)

        self.player_hand = []
        self.dealer_hand = []
        self.done = False
        self.reward = 0
        self.state = {'dealer hand': self.dealer_hand, 'player hand': self.player_hand}

        self.player_hand.append(self.cards.pop(0))
        self.dealer_hand.append(self.cards.pop(0))
        self.player_hand.append(self.cards.pop(0))
        self.dealer_hand.append(self.cards.pop(0))

        self.player_value = sum([card.number if isinstance(card.number, int) else 10 for card in self.player_hand])
        self.player_aces = sum([1 for card in self.player_hand if card.number == 11])
        self.dealer_value = sum([card.number if isinstance(card.number, int) else 10 for card in self.dealer_hand])
        self.dealer_aces = sum([1 for card in self.dealer_hand if card.number == 11])

        # acocunt for 2 aces case
        if self.player_hand[0] + self.player_hand[1] == 22:
            self.player_value -= 10

        if self.dealer_hand[0] + self.dealer_hand[1] == 21:
            self.done = True
            self.reward = 0  # does not provide any information for algorithm
        elif self.player_hand[0] + self.player_hand[1] == 21:
            self.done = True
            self.reward = 1
