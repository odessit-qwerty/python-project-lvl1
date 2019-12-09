from random import randint
from brain_games import cli


ATTEMPTS = 3
TO_WIN = 0


def get_random_number():
    return randint(0, 101)


def run(answer, user_answer, user_name):
    attempts = ATTEMPTS
    to_win = TO_WIN
    if answer == user_answer:
        print("Correct!\n")
        to_win += 1
        attempts -= 1
    else:
        cli.show_valid_answer(user_answer, answer, user_name)
        attempts -= 1
    if to_win == 3:
        cli.print_win(user_name)
