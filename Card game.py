import random

suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    # Card class will have suit and rank required for athe cards
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    # Deck class will create the 52 card required in deck using card_obj
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                card_obj = Card(suit, rank)
                self.all_cards.append(card_obj)

    def shuffle(self):  # this method will shuffle the cards in deck
        random.shuffle(self.all_cards)

    def deal_one(self):  # this method will remove the cards from deck
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)
        # print(self.all_cards.pop(0))

    def add_cards(self, new_cards):
        if type(new_cards) == type(list()):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards. '


''' Three_of_diamond = Card("Diamond","Five")
print(three_of_diamond)'''

'''my_cards = Deck()
for card in my_cards.all_cards:
    print(card)'''

# Game setup
# create the two players
player_one = Player("Player One: ")
player_two = Player("Player Two: ")

new_deck = Deck()  # create the deck
new_deck.shuffle()  # shuffle the deck

for x in range(26):  # distribute the 26 cards to each player
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
# print(len(player_one.all_cards))

game_on = True
round = 0

while game_on:
    round += 1
    print(f'Round number : {round}')

    if len(player_one.all_cards) == 0:
        print('Player One is out of card. Player Two wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two is out of card. Player One wins!')
        game_on = False
        break
    # start a new round
    player_one_cards = list()  # number of cards player one put on table, different than player_one.all_cards
    player_one_cards.append(player_one.remove_one())

    player_two_cards = list()  # number of cards player two put on table
    player_two_cards.append(player_two.remove_one())
    # print(player_two.remove_one())

    # War condition

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print('Player One Won this round')
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            print('Player Two won this round')
            at_war = False

        else:    # this is the War condition, when both player has card of same value. Player will start putting 5 cards on table
            if len(player_one.all_cards) < 5:
                print("Player One is out of card and cannot continue war, war is over. Player Two wins")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two is out of card and cannot continue war, war is over.  Player One wins")
                game_on = False
                break

            else:
                print('WAR!')
                for i in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append((player_two.remove_one()))
