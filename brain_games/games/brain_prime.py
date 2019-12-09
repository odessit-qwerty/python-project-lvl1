from brain_games import cli, engine
from brain_games.cli import ATTEMPTS


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
    attempts = ATTEMPTS
    while attempts > 0:
        number_prime = engine.get_random_number()
        if check_prime_number(number_prime) is False:
            answer = 'no'
        else:
            answer = 'yes'
        print("Questions: {}".format(number_prime))
        user_answer = cli.get_user_answer()
        engine.run(user_answer, answer, user_name)
        attempts -= 1


if __name__ == '__main__':
    main()
