import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    print(f"\nHello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.")


def load_game():
    print("""\nPlease choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    """)
    while True:
        try:
            gameNumber = int(input("Choose the game to play: "))
            if 0 < gameNumber < 4:
                break
            else:
                print("That's not a valid option!")
        except:
            print("That's not a valid option!")


    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if 0 < difficulty < 6:
                break
            else:
                print("That's not a valid option!")
        except:
            print("That's not a valid option!")


    if gameNumber == 1:
        print("\nStart playing MEMORY GAME with difficulty " + str(difficulty))
        MemoryGame.play(difficulty)

    elif gameNumber == 2:
        print("\nStart playing GUESS GAME with difficulty " + str(difficulty))
        GuessGame.play(difficulty)

    elif gameNumber == 3:
        print("\nStart playing CURRENCY ROULETTE GAME with difficulty " + str(difficulty))
        CurrencyRouletteGame.play(difficulty)


