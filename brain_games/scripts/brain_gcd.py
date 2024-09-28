#!/usr/bin/env python3


import prompt
import random
from brain_games.games.logic import get_answer


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    for attempt in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        remainder = ''
        answer = ''
        while remainder != 0:
            remainder = num1 % num2
            if remainder == 0:
                answer = num2
            else:
                num1 = num2
                num2 = remainder
        print(f'Question: {num1} {num2}')
        choice = input('Your answer: ')
        get_answer(choice, answer, name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
