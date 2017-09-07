import Deck

# todo: add a card counter accumulator to keep track of remaining cards in either player's deck
# todo: add details about how to play game to help with conveyance

# determines which 'person' gets to keep the card in each round

def turnWinner(playerValue, dealerValue, playerCard, dealerCard):

    if playerValue > dealerValue:
        playerList.extend((playerCard, dealerCard))
        print("You win this battle!")
    elif playerValue < dealerValue:
        dealerList.extend((dealerCard, playerCard))
        print("Retreat!")
    elif playerValue == dealerValue:
        print("Both sides are locked in a head to head battle, make a move!(press enter)")
        tieBreaker([])


def tieBreaker(extraList):
    # deals six cards each without showing and puts them in a list
    # makes sure there are enough cards to play the tie breaker
    if len(new_deck) >= 8:
        count = 0
        # deals cards and puts them in a list
        while count < 6:
            value, card = deck.deal_card(new_deck, 1)
            extraList.append(card)
            count = count + 1
        # deals two more cards to determine turn winner
        playerValue, playerCard = deck.deal_card(new_deck, 1)
        dealerValue, dealerCard = deck.deal_card(new_deck, 1)
        print("You drew a " + playerCard + " Your opponent drew a " + dealerCard)
        # adds 8 cards to the winner
        if playerValue > dealerValue:
            playerList.extend((playerCard, dealerCard))
            playerList.extend(extraList)
            print("You have won this battle! Take all the prisoners! (aka cards")
        elif playerValue < dealerValue:
            dealerList.extend((dealerCard, playerCard))
            dealerList.extend(extraList)
            print("Your enemy has outflanked you! Run away!")
        elif playerValue == dealerValue:
            tieBreaker(extraList)
    # handles if there are not enough cards to play a normal tie breaker
    elif 2 < len(new_deck) < 8:
        numberCards = len(new_deck) - 2
        count = 0
        # deals cards and puts them in a list
        while count < numberCards:
            value, card = deck.deal_card(new_deck, 1)
            extraList.append(card)
            count = count + 1
        # deals two more cards to determine turn winner
        addingTieBreakCards(extraList)
    elif len(new_deck) == 2:
        addingTieBreakCards(extraList)


# odd tie breaker function
def addingTieBreakCards(extraList):
    playerValue, playerCard = deck.deal_card(new_deck, 1)
    dealerValue, dealerCard = deck.deal_card(new_deck, 1)
    print("You drew a " + playerCard + " Your opponent drew a " + dealerCard)
    if playerValue > dealerValue:
        playerList.extend((playerCard, dealerCard))
        playerList.extend(extraList)
        print("You have secured a narrow victory")
    elif playerValue < dealerValue:
        dealerList.extend((dealerCard, playerCard))
        dealerList.extend(extraList)
        print("The enemy has you pinned down...time to surrender")
    elif playerValue == dealerValue:
        print("This battle has no victors")

#determines the winner of the game
def gameWinner():
    if len(dealerList) > len(playerList):
        print("You have lost this War..surrender in shame")
    elif len(playerList) > len(dealerList):
        print("You have emerged victorious in this War!")
    elif len(playerList) == len(dealerList):
        print("This War has resulted in a stalemate...there are no winners")

    # deck instance
deck = Deck.Deck()
dealerList = []
playerList = []
# creates a new deck object
new_deck = deck.create_deck()
choose = str("Press enter to begin your game of War")
input(choose)

while len(new_deck) > 0:
    choose = str("Press enter to attack")
    input(choose)
    # deals for player and dealers and returns value and card
    playerValue, playerCard = deck.deal_card(new_deck, 1)
    dealerValue, dealerCard = deck.deal_card(new_deck, 1)
    print("You drew a " + playerCard + " Your opponent drew a " + dealerCard)

    turnWinner(playerValue, dealerValue, playerCard, dealerCard)
gameWinner()

