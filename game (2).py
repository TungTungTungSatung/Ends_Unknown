import os
import time
import builtins
import TheChosenOne
def game_input(prompt_text):
    while True:
        user_choice = input(prompt_text).strip().lower()
        if user_choice == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("(Screen cleared!)\n")
            continue
        return user_choice
builtins.game_input = game_input
from game import TheChosenOne
def game_input(prompt_text):
    while True:
        user_choice = input(prompt_text).strip().lower()
        if user_choice == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("(Screen cleared!)\n")
            continue
        return user_choice
choice = input("Chose one of the following stories, remember to type exactly what the text promts you to say! In this case just right the number of the choice! Choice 1:The Chosen One")
if choice == "1":
    os.system('cls' if os.name == 'nt' else 'clear') 
    speed = input("What is your reading speed 1 is fast 2 is average 3 is slow!: ")
    if speed == "1":
        os.system('cls' if os.name == 'nt' else 'clear') 
        TheChosenOneFast.main()
    elif speed == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        TheChosenOne.main()
    elif speed == "3":
        os.system('cls' if os.name == 'nt' else 'clear') 
        TheChosenOneSlow.main()
  