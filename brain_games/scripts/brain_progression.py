#!/usr/bin/env python3


import prompt
import random
from brain_games.games.logic import get_answer


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    for attempt in range(3):
        new_list = []
        stop = random.randint(5, 10)
        num = random.randint(1, 20)
        step = random.randint(1, 10)
        ind = random.randint(0, stop - 1)
        for x in range(stop):
            new_list.append(str(num))
            num += step
        answer = new_list[ind]
        new_l = new_list[:]
        new_l[ind] = '..'
        new_l = ' '.join(new_l)
        print(f'Question: {new_l}')
        player_choice = input('Your answer: ')
        get_answer(player_choice, answer, name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
