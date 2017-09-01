class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        print("%s of %s") % (self.rank, self.suit)
