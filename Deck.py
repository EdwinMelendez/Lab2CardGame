import random
import Card


class Deck:
    def __init__(self):
        self.deck = []
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.suits = ["Spades", "Diamonds", "Clubs", "Hearts"]

        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append(Card.Card(rank, suit))

            random.shuffle(self.deck)

    def printDeck(self):
        for card in self.deck:
            print(card.__str__())