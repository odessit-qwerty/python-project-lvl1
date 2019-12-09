from brain_games import cli, engine
from random import randint
from brain_games.engine import ATTEMPTS


operation_list = ['+', '-', '*']


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
    attempts = ATTEMPTS
    while attempts > 0:
        num_first = engine.get_random_number()
        num_second = engine.get_random_number()
        operation = operation_list[randint(0, len(operation_list) - 1)]
        answer = get_correct_answer(num_first, num_second, operation)
        print("Question: {} {} {}".format(num_first, operation, num_second))
        user_answer = cli.get_user_answer()
        engine.run(answer, user_answer, user_name)
        attempts -= 1


if __name__ == '__main__':
    main()
