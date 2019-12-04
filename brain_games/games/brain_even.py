from brain_games.cli import get_correct_answer, get_user_answer, get_user_name, get_questions, welcome


def get_correct_answer(questions):
    if questions % 2 == 0:
        return 'yes'
    else:
        return 'no'


def main():
    welcome()
    user_name = get_user_name()
    attempt = 3
    to_win = 0
    while attempt > 0:
        questions = get_questions()
        answer = get_correct_answer(questions)
        print("Question: {}".format(questions))
        user_answer = get_user_answer()
        if answer == user_answer:
            print("Correct!\n")
            to_win += 1
            attempt -= 1
        else:
            print(""""{}" is wrong answer ;(. Correct answer was "{}".
Let's try again {}!\n""".format(user_answer, answer, user_name))
            attempt -= 1
        if to_win == 3:
            print("Congratulations, {}!".format(user_name))
            return False


if __name__ == "__main__":
    main()
