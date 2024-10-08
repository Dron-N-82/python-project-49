import prompt


def play(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.description)
    for _ in range(3):
        choice, answer = game.get_choice_and_answer()
        if choice == str(answer):
            print('Correct!')
        else:
            print(f"'{choice}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            break
        print(f'Congratulations, {name}!')
