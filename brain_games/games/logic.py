def get_answer(player_choice, answer, name):
    if player_choice == str(answer):
        print('Correct!')
    else:
        print(f"'{player_choice}' is wrong answer ;(. Correct answer was '{answer}'.")
        print(f"Let's try again, {name}!")
        exit()
