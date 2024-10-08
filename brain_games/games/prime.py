import random

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_choice_and_answer():
    answer = ''
    number = random.randint(1, 100)
    print(f'Question: {number}')
    choice = input('Your answer: ')
    divider = 2
    while number % divider != 0:
        divider += 1
    answer = 'yes' if divider == number else 'no'
    return choice, answer
