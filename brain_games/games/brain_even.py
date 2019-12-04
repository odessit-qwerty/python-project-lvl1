<<<<<<< HEAD
from brain_games import cli
from brain_games.cli import ATTEMPT, TO_WIN
from random import randint
=======
from brain_games.cli import get_correct_answer, get_user_answer, get_user_name, get_questions, welcome
>>>>>>> b095c7454fff1ab4e7a35ae75ac70820cd8b220a


def get_correct_answer(questions):
    if questions % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
<<<<<<< HEAD
    print("""
Welcome to the Brain Games!
Answer "yes" if number even otherwise answer "no"\n""")
    user_name = cli.get_user_name()
    attempt = ATTEMPT
    to_win = TO_WIN
    while attempt > 0:
        questions = randint(0, 101)
        answer = get_correct_answer(questions)
        print("Question: {}".format(questions))
        user_answer = cli.get_user_answer()
=======
    welcome()
    user_name = get_user_name()
    attempt = 3
    to_win = 0
    while attempt > 0:
        questions = get_questions()
        answer = get_correct_answer(questions)
        print("Question: {}".format(questions))
        user_answer = get_user_answer()
>>>>>>> b095c7454fff1ab4e7a35ae75ac70820cd8b220a
        if answer == user_answer:
            print("Correct!\n")
            to_win += 1
            attempt -= 1
        else:
<<<<<<< HEAD
            cli.valid_answer(user_answer, answer, user_name)
            attempt -= 1
        if to_win == 3:
            cli.check_win(user_name)
=======
            print(""""{}" is wrong answer ;(. Correct answer was "{}".
Let's try again {}!\n""".format(user_answer, answer, user_name))
            attempt -= 1
        if to_win == 3:
            print("Congratulations, {}!".format(user_name))
            return False
>>>>>>> b095c7454fff1ab4e7a35ae75ac70820cd8b220a


if __name__ == "__main__":
    main()
