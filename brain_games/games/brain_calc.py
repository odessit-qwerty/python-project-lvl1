from brain_games import cli, engine
from brain_games.engine import ATTEMPT, TO_WIN
from random import randint


def get_correct_answer(num_first, num_second, operation):
    if operation == '+':
        return str(num_first + num_second)
    elif operation == '-':
        return str(num_first - num_second)
    elif operation == '*':
        return str(num_first * num_second)


def main():
    print("""
Welcome to the Brain Games!
What is the result of the expression?\n""")
    user_name = cli.get_user_name()
    attempt = ATTEMPT
    to_win = TO_WIN
    operation_list = ['+', '-', '*']
    while attempt > 0:
        num_first = engine.get_random_number()
        num_second = engine.get_random_number()
        operation = operation_list[randint(0, len(operation_list) - 1)]
        answer = get_correct_answer(num_first, num_second, operation)
        print("Question: {} {} {}".format(num_first, operation, num_second))
        user_answer = cli.get_user_answer()
        if answer == user_answer:
            print("Correct!\n")
            to_win += 1
            attempt -= 1
        else:
            cli.show_valid_answer(user_answer, answer, user_name)
            attempt -= 1
        if to_win == 3:
            cli.check_win(user_name)
