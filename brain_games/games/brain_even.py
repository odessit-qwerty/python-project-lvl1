from brain_games import cli, engine
from brain_games.engine import ATTEMPTS


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
    attempts = ATTEMPTS
    while attempts > 0:
        questions = engine.get_random_number()
        answer = get_correct_answer(questions)
        print("Question: {}".format(questions))
        user_answer = cli.get_user_answer()
        engine.run(user_answer, answer, user_name)
        attempts -= 1


if __name__ == "__main__":
    main()
