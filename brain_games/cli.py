#!/usr/bin/env python3
import prompt
<<<<<<< HEAD

ATTEMPT = 3
TO_WIN = 0
=======
import random


def welcome():
    print("""
                       Welcome to the Brain Games!
             Answer "yes" if number even otherwise answer "no"\n""")
>>>>>>> b095c7454fff1ab4e7a35ae75ac70820cd8b220a


def get_user_name():
    name = prompt.string("May I have your name? ")
    print("Hello {}!\n".format(name))
    return name


def get_user_answer():
    return prompt.string("Your answer: ")


<<<<<<< HEAD
def valid_answer(user_answer, answer, user_name):
    print(""""{}" is wrong answer ;(. Correct answer was "{}".
Let's try again {}!\n""".format(user_answer, answer, user_name))


def check_win(user_name):
    print("Congratulations, {}!".format(user_name))
    return False
=======
def get_correct_answer():
    if questions % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_questions():
    return random.randint(0, 101)


if __name__ == "__main__":
    welcome()
>>>>>>> b095c7454fff1ab4e7a35ae75ac70820cd8b220a
