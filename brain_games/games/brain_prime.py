from brain_games import cli, engine
from brain_games.cli import ATTEMPT, TO_WIN


def check_prime_number(number):
    if number <= 1:
        return False
    for value in range(2, int(number ** 0.5) + 1):
        if (number % value) == 0:
            return False
    return True


def main():
    print("""
Welcome to the Brain Games!
Answer "yes" if given number is prime. Otherwise answer "no".\n""")
    user_name = cli.get_user_name()
    attempt = ATTEMPT
    to_win = TO_WIN
    while attempt > 0:
        number_prime = engine.get_random_number()
        if check_prime_number(number_prime) is False:
            answer = 'no'
        else:
            answer = 'yes'
        print("Questions: {}".format(number_prime))
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


if __name__ == '__main__':
    main()
