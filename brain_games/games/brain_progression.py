from brain_games import cli, engine
from brain_games.engine import ATTEMPTS
from random import randint


def make_progression():
    progression_length = 10
    step = randint(1, 10)
    progression_first_number = randint(1, 10)
    hidden_element_index = randint(0, progression_length - 1)
    question = ''
    counter = 0
    while counter < progression_length:
        next_in_progression = progression_first_number + counter * step
        if counter == hidden_element_index:
            correct_answer = next_in_progression
            question = ('{}..'.format(question))
            counter = counter + 1
        else:
            question = ('{}{}'.format(question, next_in_progression))
            counter = counter + 1
    return question, str(correct_answer)


def main():
    print("""
Welcome to the Brain Games!
What number is missing in the progression?\n""")
    user_name = cli.get_user_name()
    attempts = ATTEMPTS
    while attempts > 0:
        progression, answer = make_progression()
        print("Question: {}".format(progression))
        user_answer = cli.get_user_answer()
        engine.run(user_answer, answer, user_name)
        attempts -= 1


if __name__ == '__main__':
    main()
