#!/usr/bin/env python3


import prompt
import random
import operator
from brain_games.games.logic import get_answer


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    for attempt in range(3):
        operate = ''
        answer = ''
        num1 = random.randint(1, 25)
        num2 = random.randint(1, 25)
        oper = random.choice([operator.add, operator.sub, operator.mul])
        if oper == operator.add:
            operate = '+'
            answer = operator.add(num1, num2)
        elif oper == operator.sub:
            operate = '-'
            answer = operator.sub(num1, num2)
        elif oper == operator.mul:
            operate = '*'
            answer = operator.mul(num1, num2)
        print(f'Question: {num1} {operate} {num2}')
        choice = input('Your answer: ')
        get_answer(choice, answer, name)
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
