class Card:

    def __init__(self, suit, value, points):
        self.suit = suit
        self.value = value
        self.points = points
    
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.hand = []

    def info(self):
        if self.name == "Bob":
            print(f'Dealer {self.name} has {self.hand[0]}')
        else:
            print(f'Player {self.name} has {self.hand} which give him {self.points}')

    def end_game(self):
        if self.name == "Bob":
            print(f'Dealer {self.name} has {self.hand} which give him {self.points}')
        else:
            print(f'Player {self.name} has {self.hand} which give him {self.points}')