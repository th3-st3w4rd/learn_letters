from time import sleep
from random import choice
from pretext import Introductions

import argparse

from game_content import GameContent
from gb_responses import victories, defeats


def play(game_content):
    user_correct = 0
    user_incorrect = 0
    intro = Introductions()
    while True:
        rando_lett = choice(game_content)
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
            break
        else:
            print("an error has occured")
        print(f"CORRECT: {user_correct} INCORRECT: {user_incorrect}\n")
        sleep(0.5)
    return (user_correct, user_incorrect)

def main():
    parser = argparse.ArgumentParser(prog="Learn Letters", description="Practice typing, reading, and matching letters & symbols.", usage="python (or python3) learn_letters.py -l -L -n -s")
    parser.add_argument("-l","--lower-letters",action="store_true", help="Includes 'lowercase letters' when loading the game.")
    parser.add_argument("-L","--upper-letters",action="store_true", help="Includes 'uppercase letters' when loading the game.")
    parser.add_argument("-n","--numbers",action="store_true", help="Includes 'numbers' when loading the game.")
    parser.add_argument("-s","--symbols",action="store_true", help="Includes 'symbols' when loading the game.")
    args = parser.parse_args()
    content = GameContent(args)
    score = play(content.active_modules)
    print(f"Final Score: {score[0]} CORRECT | {score[1]} INCORRECT\n")

if __name__ == "__main__":
    main()
