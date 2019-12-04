from brain_games import cli
from brain_games.cli import ATTEMPT, TO_WIN
from random import randint


def get_correct_answer(questions):
    if questions % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
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
        if answer == user_answer:
            print("Correct!\n")
            to_win += 1
            attempt -= 1
        else:
            cli.valid_answer(user_answer, answer, user_name)
            attempt -= 1
        if to_win == 3:
            cli.check_win(user_name)


if __name__ == "__main__":
    main()
