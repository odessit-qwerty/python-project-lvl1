from brain_games import cli, engine
from brain_games.engine import ATTEMPTS
from math import gcd


def main():
    print("""
Welcome to the Brain Games!
Find the greatest common divisor of given numbers.\n""")
    user_name = cli.get_user_name()
    attempts = ATTEMPTS
    while attempts > 0:
        number_first = engine.get_random_number()
        number_second = engine.get_random_number()
        answer = str(gcd(number_first, number_second))
        print("Question: {} {}".format(number_first, number_second))
        user_answer = cli.get_user_answer()
        engine.run(user_answer, answer, user_name)
        attempts -= 1


if __name__ == '__main__':
    main()
