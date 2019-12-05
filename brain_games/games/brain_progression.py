from brain_games import cli, engine
from brain_games.engine import ATTEMPT, TO_WIN
from random import randint

def make_progression():
    progression_length = 10
    progression_step = randint(1, 10)
    progression_first_number = randint(1, 10)
    hidden_element_index = randint(0, progression_length - 1)
    question = ''
    counter = 0
    while counter < progression_length:
        next_in_progression = progression_first_number + counter * progression_step
        if counter == hidden_element_index:
            correct_answer = next_in_progression
            question = ('{}.. '.format(question))
            counter = counter + 1
        else:
            question = ('{}{} '.format(question, next_in_progression))
            counter = counter + 1
    return question, str(correct_answer)
        

def main():
    print("""
Welcome to the Brain Games!
What number is missing in the progression?\n""")
    user_name = cli.get_user_name()
    attempt = ATTEMPT
    to_win = TO_WIN
    while attempt > 0:
        progression, answer = make_progression()
        print("Question: {}".format(progression))
        user_answer = cli.get_user_answer()
        if answer == user_answer:
            print("Correct!\n")
            to_win += 1
            attempt -= 1
        else:
            cli.show_valid_answer(user_answer, answer, user_name)
            attempt -= 1
        if to_win == 3:
            cli.print_win(user_name)
        
