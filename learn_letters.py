"""
Helps kindergarteners to learn letters and typing.
"""
from time import sleep
from random import choice
from gb_responses import victories, defeats

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
    ]
capitol_alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
    ]
intro = "Hello!  My name is G34r-B0lt! GB for short."
goals = "My goal is to help you practice your letters, numbers, symbols, and typing!"
instructions = "I'll show a letter to the screen and you try to match it!"
how_to_close = "If at any point you want to stop playing, enter '--'"
salutation = "Happy learning!\n"
combined_alphabet = alphabet + capitol_alphabet
#rando_lett = choice(combined_alphabet)
def play():
    user_correct = 0
    user_incorrect = 0 
    play = True
    print(intro)
    sleep(1)
    print(goals)
    sleep(1)
    print(instructions)
    sleep(.5)
    print(how_to_close)
    sleep(.5)
    print(salutation)
    sleep(.25)
    while play:
        rando_lett = choice(combined_alphabet)
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
            sleep(.5)
            print("Thank you for playing!")
            sleep(1)
            play = False
        else:
            print("an error has occured")
        print(f"CORRECT: {user_correct} INCORRECT: {user_incorrect}\n")
        sleep(.5)

if __name__ == "__main__":
    play()
