import Deck


# determines which 'person' gets to keep the card in each round

def turnWinner(playerValue, dealerValue, playerCard, dealerCard):
    if playerValue > dealerValue:
        playerList.append(playerCard)
    elif playerValue < dealerValue:
        dealerList.append(dealerCard)

# todo: add a def for war, when each player has the same rank, lays down 3 cards then flips the 4th, winner takes all

# todo: also make sure that if the 4th card flipped is the same rank you repeat war til a winner emerges
# deck instance
deck = Deck.Deck()
dealerList = []
playerList = []
# creates a new deck object
new_deck = deck.create_deck()

# first parameter asks for deck dictionary, second asks for how many cards to be dealt then prints keys
# deck.deal_card(new_deck, 7)

# deals for player and dealers and returns value and card
playerValue, playerCard = deck.deal_card(new_deck, 1)
dealerValue, dealerCard = deck.deal_card(new_deck, 1)
turnWinner(playerValue, dealerValue, playerCard, dealerCard)

print(playerCard)
print(dealerCard)
print(playerList)
print(dealerList)
