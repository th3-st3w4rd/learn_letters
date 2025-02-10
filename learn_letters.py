"""
Helps kindergarteners to learn letters and typing.
"""

from time import sleep
from random import choice
from pretext import Introductions
from game_content import GameContent
from gb_responses import victories, defeats


def play():
    user_correct = 0
    user_incorrect = 0
    play = True
    intro = Introductions()
    game_setup = GameContent()
    while play:
        rando_lett = choice(game_setup.active_modules)
        print(f"GB: Try to match: '{rando_lett}'")
        user_input = input("What letter do you see? ")
        if rando_lett == user_input:
            print("CORRECT")
            print(choice(victories))
            user_correct += 1
        elif rando_lett != user_input and user_input != "--":
            print("NOT CORRECT")
            print(choice(defeats))
            user_incorrect += 1
        elif user_input == "--":
            print("Quitting the game!")
            sleep(0.5)
            print("Thank you for playing!")
            sleep(1)
            play = False
        else:
            print("an error has occured")
        print(f"CORRECT: {user_correct} INCORRECT: {user_incorrect}\n")
        sleep(0.5)


if __name__ == "__main__":
    play()
