import random


description = 'Find the greatest common divisor of given numbers.'


def get_choice_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    remainder = ''
    answer = ''
    while remainder != 0:
        remainder = num1 % num2
        if remainder == 0:
            answer = num2
        else:
            num1, num2 = num2, remainder
    print(f'Question: {num1} {num2}')
    choice = input('Your answer: ')
    return choice, answer
