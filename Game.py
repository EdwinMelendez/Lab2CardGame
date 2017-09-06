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
    #makes sure there are enough cards to play the tie breaker
    if len(new_deck) >= 8:
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
    #handles if there are not enough cards to play a normal tie breaker
    elif 2 < len(new_deck) < 8:
        numberCards = len(new_deck) -2
        extraList = []
        count = 0
        # deals cards and puts them in a list
        while count < numberCards:
            Value, Card = deck.deal_card(new_deck, 1)
            extraList.append(Card)
            count = count + 1
        # deals two more cards to determine turn winner
            addingTieBreakCards(extraList)
            print("eight")

    elif len(new_deck) ==2:
        extraList = []
        addingTieBreakCards(extraList)
        print("two")
#odd tie breaker function
def addingTieBreakCards(extraList):
    extraList = extraList
    playerValue, playerCard = deck.deal_card(new_deck, 1)
    dealerValue, dealerCard = deck.deal_card(new_deck, 1)
    if playerValue > dealerValue:
        playerList.extend((playerCard, dealerCard))
        playerList.extend(extraList)
    elif playerValue < dealerValue:
        dealerList.extend((dealerCard, playerCard))
        dealerList.extend(extraList)
    elif playerValue == dealerValue:
        print("Its a draw! These cards will be discarded")
#determines the winner of the game
def gameWinner():
    if len(dealerList) > len(playerList):
        print("You lose")
    elif len(playerList) > len(dealerList):
        print("You win")
    elif len(playerList) == len(dealerList):
        print("tie")

    # deck instance
deck = Deck.Deck()
dealerList = []
playerList = []
    # creates a new deck object
new_deck = deck.create_deck()

# first parameter asks for deck dictionary, second asks for how many cards to be dealt then prints keys
# deck.deal_card(new_deck, 7)
while len(new_deck) > 0:
    # deals for player and dealers and returns value and card
    playerValue, playerCard = deck.deal_card(new_deck, 1)
    dealerValue, dealerCard = deck.deal_card(new_deck, 1)
    turnWinner(playerValue, dealerValue, playerCard, dealerCard)
gameWinner()

print(dealerList)
print(playerList)