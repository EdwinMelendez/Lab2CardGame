import random

# Adapted from Andy's text book


class Deck:

    def create_deck(self):

        # creates dictionary of cards and their values
        # stored as key-value pairs
        deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4,
                '5 of Spades': 5, '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8,
                '9 of Spades': 9, '10 of Spades': 10, 'Jack of Spades': 11, 'Queen of Spades': 12,
                'King of Spades': 13,

                'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4,
                '5 of Hearts': 5, '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8,
                '9 of Hearts': 9, '10 of Hearts': 10, 'Jack of Hearts': 11, 'Queen of Hearts': 12,
                'King of Hearts': 13,

                'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4,
                '5 of Diamonds': 5, '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8,
                '9 of Diamonds': 9, '10 of Diamonds': 10, 'Jack of Diamonds': 11, 'Queen of Diamonds': 12,
                'King of Diamonds': 13,

                'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4,
                '5 of Clubs': 5, '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8,
                '9 of Clubs': 9, '10 of Clubs': 10, 'Jack of Clubs': 11, 'Queen of Clubs': 12,
                'King of Clubs': 13}

        return deck

    def deal_card(self, deck, number):
        # creates a list of deck keys
        shuffled_deck = list(deck.keys())

        # shuffles list of keys
        random.shuffle(shuffled_deck)

        # accumulator for hand
        hand_value = 0

        # makes sure the cards being dealt does not exceed the size of the deck
        if number > len(deck):
            number = len(deck)

        # deals the cards and their values
        for count in range(number):
            # grabs a random key from the list
            card = shuffled_deck.pop()
            # uses that key to get the value of the card
            value = deck.pop(card)
            hand_value += value
            return value, card
