from brain_games import cli, engine
from brain_games.cli import ATTEMPT, TO_WIN
from math import gcd


def main():
    print("""
Welcome to the Brain Games!
Find the greatest common divisor of given numbers.\n""")
    user_name = cli.get_user_name()
    attempt = ATTEMPT
    to_win = TO_WIN
    while attempt > 0:
        number_first = engine.get_random_number()
        number_second = engine.get_random_number()
        answer = str(gcd(number_first, number_second))
        print("Question: {} {}".format(number_first, number_second))
        user_answer = cli.get_user_answer()
        if answer == user_answer:
            print("Correct!\n")
            to_win += 1
            attempt -= 1
        else:
            cli.show_valid_answer(user_answer, answer, user_name)
            attempt -= 1
        if to_win == 3:
            cli.print_win(user_name)
