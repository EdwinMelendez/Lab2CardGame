import Deck


# determines which 'person' gets to keep the card in each round

def turnWinner(playerValue, dealerValue, playerCard, dealerCard):
    if playerValue > dealerValue:
        playerList.extend((playerCard, dealerCard))
    elif playerValue < dealerValue:
        dealerList.extend((dealerCard, playerCard))
    elif playerValue == dealerValue:
        tieBreaker()

        
def tieBreaker():
    # deals six cards each without showing and puts them in a list
    extraList = []
    count = 0
    # deals cards and puts them in a list
    while count < 6:
        Value, Card = deck.deal_card(new_deck, 1)
        extraList.append(Card)
        count = count + 1
    # deals two more cards to determine turn winner
    playerValue, playerCard = deck.deal_card(new_deck, 1)
    dealerValue, dealerCard = deck.deal_card(new_deck, 1)
    # adds 8 cards to the winner
    if playerValue > dealerValue:
        playerList.extend((playerCard, dealerCard))
        playerList.extend(extraList)
    elif playerValue < dealerValue:
        dealerList.extend((dealerCard, playerCard))
        dealerList.extend(extraList)
    elif playerValue == dealerValue:
        tieBreaker()
# todo: keep the game going until the deck runs out
# todo: add up the cards in each list to determine winner

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


print(dealerList)
print(playerList)