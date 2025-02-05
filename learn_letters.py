"""
Helps kindergarteners to learn letters and typing.
"""
from time import sleep
from random import choice
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
combined_alphabet = alphabet + capitol_alphabet
def play():
    play = True
    print("Type '--' to quit the game!\n")
    while play:
        rando_lett = choice(combined_alphabet)
        print(f"Computer sees: {rando_lett}")
        user_input = input("What letter do you see? ")
        if rando_lett == user_input:
            print("Booya!! You got it correct!  Good Job!")
        elif rando_lett != user_input and user_input != "--":
            print("Oh no! Those letters don't match!")
        elif user_input == "--":
            print("Quitting the game!")
            sleep(.5)
            print("Thank you for playing!")
            sleep(1)
            play = False
        else:
            print("an error has occured")
        print("")
        sleep(.5)

if __name__ == "__main__":
    play()
