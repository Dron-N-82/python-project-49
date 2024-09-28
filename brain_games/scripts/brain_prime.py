#!/usr/bin/env python3


import random
import prompt
from brain_games.games.logic import get_answer


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    for attempt in range(3):
        answer = ''
        number = random.randint(1, 100)
        print(f'Question: {number}')
        choice = input('Your answer: ')
        divider = 2
        while number % divider != 0:
            divider += 1
        if divider == number:
            answer = 'yes'
            get_answer(choice, answer, name)
        else:
            answer = 'no'
            get_answer(choice, answer, name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
