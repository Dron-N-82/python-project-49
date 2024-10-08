import random


description = 'What number is missing in the progression?'


def get_choice_and_answer():
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
    choice = input('Your answer: ')
    return choice, answer
