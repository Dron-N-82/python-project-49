def get_answer(choice, answer, name):
    if choice == str(answer):
        print('Correct!')
    else:
        print(f"'{choice}' is wrong answer ;(. Correct answer was '{answer}'.")
        print(f"Let's try again, {name}!")
        exit()
