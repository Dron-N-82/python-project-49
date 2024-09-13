#!/usr/bin/env python3


import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for attempt in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        player_choice = input('Your answer: ')
        if number % 2 == 0:
            if player_choice == 'yes':
                print('Correct!')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
        elif number % 2 == 1:
            if player_choice == 'no':
                print('Correct!')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
