from random import choice
import classes
import functions

def game():
    
    i = 0
    global cards_values

    deck = functions.create_deck()

    player_name = input('Whats Your name?')
    oPlayer = classes.Player(player_name)
    oDealer = classes.Player("Bob")

    while i < 2:
        card = choice(deck)
        oPlayer.hand.append([card.value, card.suit])
        deck.remove(card)
        oPlayer.points += card.points

        card = choice(deck)
        oDealer.hand.append([card.value, card.suit])
        deck.remove(card)
        oDealer.points += card.points

        i += 1

    if oPlayer.hand[0][0] == oPlayer.hand[1][0]:  # two aces
        oPlayer.points = 12 # 11 + 1

    if oDealer.hand[0][0] == oDealer.hand[1][0]:  # two aces
        oDealer.points = 12 # 11 + 1

    oPlayer.info()
    oDealer.info()

    
    functions.play(oPlayer, oDealer, deck)

def main():
    game()

if __name__ == '__main__':
    main()