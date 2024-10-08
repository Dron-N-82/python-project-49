import random
import operator


description = 'What is the result of the expression?'


def get_choice_and_answer():
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
    return choice, answer
