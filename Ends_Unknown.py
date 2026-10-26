
import os


def game_input(prompt_text):
    while True:
        user_choice = input(prompt_text).strip().lower()

        if user_choice == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            print("(Screen cleared!)\n")
            continue

        return user_choice
