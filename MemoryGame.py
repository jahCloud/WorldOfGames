import random
import time
from Mytools import cls


def generate_sequence(difficulty):
    random_numbers = [random.randrange(1, 101) for i in range(difficulty)]
    print(random_numbers)
    time.sleep(0.7)
    cls()
    return random_numbers


def get_list_from_user(difficulty):
    print("Enter the numbers you saw, separately")
    inputs = []
    for i in range(difficulty):
        inputs.append(input("Number: "))
    return inputs


def is_list_equal(list_a, list_b):
    if list_a == list_b:
        print("\nYou WIN ! The numbers were indeed: ", str(list_a))
    else:
        print("\nGame Over! The numbers were: ", str(list_a))
        exit()
        return False


def play(difficulty):
    random_list = generate_sequence(difficulty)
    user_list = get_list_from_user(len(random_list))
    is_succeed = is_list_equal(random_list, list(map(int, user_list)))
    return is_succeed
