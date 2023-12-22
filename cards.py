# cards.py

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = int(rank) if rank.isnumeric() else 10
        self.value = 11 if rank == 'Ace' else self.value

    def __str__(self):
        return self.rank + " of " + self.suit
    
    def setValue(self, value):
        self.value = value

class Deck:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.shuffle()

    def __str__(self):
        return self.name + ": " + str(len(self.cards)) + " cards in deck. Top card is " + str(self.cards[0]) if len(self.cards) > 0 else "The deck is empty."

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        card = self.cards[0] # return top card
        self.cards.remove(card)
        return card
    
    def add_card_to_deck(self, card):
        self.cards.append(card)