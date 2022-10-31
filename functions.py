from random import choice, randint
from classes import Card
import time

def create_deck():

    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    cards_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

    deck = []
    number_of_decks = randint(1, 8)
    for _ in range(number_of_decks):
        for suit in suits:
            for card in cards:
                deck.append(Card(suit, card, cards_values[card]))
    return deck

def check_score(Player, Dealer):
    Player.end_game()
    print("Dealer is revealing his cards:")
    Dealer.end_game()
    if Player.points == Dealer.points == 21:
        print('It is a TIE!')
        time.sleep(10)
    elif Player.points == 21:
        print("Player has a blackjack!!!\nPLAYER WINS!")
        time.sleep(10)
    elif Player.points > 21:
        print("Player lose the game!")
        time.sleep(10)
    elif Dealer.points == 21:
        print("Dealer has a blackjack!!!\nDEALER WINS!")
        time.sleep(10)
    elif Player.points > Dealer.points:
        print("Player WINS!")
        time.sleep(10)
    else:
        print("Dealer WINS!")
        time.sleep(10)

def play(Player, Dealer, deck):
    while Player.points < 21:
        print(f'{Player.name} what do You want to do?')
        print('Type H to Hit or S to Stand')
        decision = input()
        if len(decision) != 1 or decision.upper() != "H" and decision.upper() != "S":
            print("Wrong choice! Try again!")
        if decision.upper() == "H":
            card = choice(deck)
            Player.hand.append([card.value, card.suit])
            deck.remove(card)
            Player.points += card.points
            Player.info()
            Dealer.info()
        if decision.upper() == "S":
            break
    
    while Dealer.points < 17:
        print("Dealer choose to HIT")
        card = choice(deck)
        Dealer.hand.append([card.value, card.suit])
        deck.remove(card)
        Dealer.points += card.points
    
    check_score(Player, Dealer)
