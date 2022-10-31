from game import game

def main():
    while True:
        print()
        print("*" * 57)
        print("*" + " " * 55 + "*")
        print("*        Hello Player! This is a BLACKJACK GAME         *")
        print("* This Game is created by Jakub Kowalski form POLAND/EU *")
        print("*" + " " * 55 + "*")
        print("*" * 57)

        print("\nTo START THE GAME type P")
        print("\nTo QUIT THE GAME type Q\n")
        decision2 = input()
        if len(decision2) != 1 or decision2.upper() != "P" and decision2.upper() != "Q":
            print("Wrong choice! Try again!")
        if decision2.upper() == "P":
            game()
        elif decision2.upper() == "Q":
            print("GOODBYE!")
            quit()

if __name__ == "__main__":
    main()
    
    