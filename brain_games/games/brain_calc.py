from brain_games.cli import get_user_answer, get_user_name, valid_answer, check_win
from brain_games.cli import ATTEMPT, TO_WIN
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
    user_name = get_user_name()
    attempt = ATTEMPT
    to_win = TO_WIN
    operation_list = ['+','-','*']
    while attempt > 0:
        num_first = randint(0, 101)
        num_second = randint(0, 101)
        operation = operation_list[randint(0, len(operation_list) - 1)]
        answer = get_correct_answer(num_first, num_second, operation)
        print("Question: {} {} {}".format(num_first, operation, num_second))
        user_answer = get_user_answer()
        if answer == user_answer:
            print("Correct!\n")
            to_win += 1
            attempt -= 1
        else:
            valid_answer(user_answer, answer, user_name)
            attempt -= 1
        if to_win == 3:
            check_win(user_name)
