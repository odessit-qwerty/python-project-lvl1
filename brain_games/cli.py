#!/usr/bin/env python3
import prompt
from random import randint

ATTEMPT = 3
TO_WIN = 0


def get_user_name():
    name = prompt.string("May I have your name? ")
    print("Hello {}!\n".format(name))
    return name


def get_user_answer():
    return prompt.string("Your answer: ")


def show_valid_answer(user_answer, answer, user_name):
    print(""""{}" is wrong answer ;(. Correct answer was "{}".
Let's try again {}!\n""".format(user_answer, answer, user_name))


def print_win(user_name):
    print("Congratulations, {}!".format(user_name))
    return False
