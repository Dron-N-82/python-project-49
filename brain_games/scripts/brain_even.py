#!/usr/bin/env python3


import prompt
import random
from brain_games.games.logic import get_answer


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for attempt in range(3):
        answer = ''
        number = random.randint(1, 100)
        print(f'Question: {number}')
        player_choice = input('Your answer: ')
        if number % 2 == 0:
            answer = 'yes'
            get_answer(player_choice, answer, name)
        elif number % 2 == 1:
            answer = 'no'
            get_answer(player_choice, answer, name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
