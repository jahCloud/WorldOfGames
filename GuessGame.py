import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    print(secret_number)
    return secret_number


def get_guess_from_user(difficulty):
    guess_from_user = int(input("Enter a number between 1 and " + str(difficulty) + ": "))
    print("Your guess: ", guess_from_user)
    return guess_from_user


def compare_results(secret_number, guess_from_user):
    if guess_from_user == secret_number:
        print("You Win !!!")
        return True
    else:
        print("Game Over !!!")
        return False


def play(difficulty):
    random_list = generate_number(difficulty)
    user_list = get_guess_from_user(difficulty)
    has_won = compare_results(random_list, user_list)

    return has_won
