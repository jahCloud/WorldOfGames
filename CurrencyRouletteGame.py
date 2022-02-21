from currency_converter import CurrencyConverter
import random

# Source: https://pypi.org/project/CurrencyConverter/

r = random.randint(1, 100)
c = c = CurrencyConverter()
t = int(c.convert(r, 'USD', 'ILS'))


def get_money_interval(user_guess, d):
    max_value = t + (5 - d)
    min_value = t - (5 - d)
    has_won = max_value > user_guess > min_value
    return print("\nUser has won: ", has_won, "\n\nConvert Calculation is: ", t, "\nAnswer Range is between ", min_value, " and ", max_value, "\nYour Guess is: ", user_guess)


def get_guess_from_user():
    guess = input("Guess the value of " + str(r) + " USD in ILS: ")
    return int(guess)


def play(difficulty):
    d = int(difficulty)
    return get_money_interval(get_guess_from_user(), d)





