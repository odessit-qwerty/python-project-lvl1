#!/usr/bin/env python3
import prompt
import random


def welcome():
    print("""
                       Welcome to the Brain Games!
             Answer "yes" if number even otherwise answer "no"\n""")


def get_user_name():
    name = prompt.string("May I have your name? ")
    print("Hello {}!\n".format(name))
    return name


def get_user_answer():
    return prompt.string("Your answer: ")


def get_correct_answer():
    if questions % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_questions():
    return random.randint(0, 101)


if __name__ == "__main__":
    welcome()
