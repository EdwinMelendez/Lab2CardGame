import Deck
#determines which 'person' gets to keep the card in each round
def turnWinner(playerValue, dealerValue, playerCard, dealerCard):
    if playerValue > dealerValue:
        playerList.append(playerCard)
    elif playerValue < dealerValue:
        dealerList.append(dealerCard)



# deck instance
deck = Deck.Deck()
dealerList = []
playerList = []
# creates a new deck object
new_deck = deck.create_deck()

# first parameter asks for deck dictionary, second asks for how many cards to be dealt then prints keys
#deck.deal_card(new_deck, 7)

#deals for player and dealers and returns value and card
playerValue, playerCard = deck.deal_card(new_deck, 1)
dealerValue, dealerCard = deck.deal_card(new_deck, 1)
turnWinner(playerValue, dealerValue, playerCard, dealerCard)

print(playerCard)
print(dealerCard)
print(playerList)
print(dealerList)








