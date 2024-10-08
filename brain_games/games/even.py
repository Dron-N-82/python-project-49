import random

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_choice_and_answer():
    answer = ''
    number = random.randint(1, 100)
    print(f'Question: {number}')
    choice = input('Your answer: ')
    answer = 'yes' if number % 2 == 0 else 'no'
    return choice, answer
