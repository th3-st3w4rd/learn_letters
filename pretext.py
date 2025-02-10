from time import sleep


class Introductions:
    def __init__(self):
        self.intro = "Hello!  My name is G34r-B0lt! GB for short."
        self.goals = "My goal is to help you practice your letters, numbers, symbols, and typing!"
        self.instructions = "I'll show a letter to the screen and you try to match it!"
        self.how_to_close = "If at any point you want to stop playing, enter '--'"
        self.salutation = "Happy learning!\n"

        print(self.intro)
        sleep(1)
        print(self.goals)
        sleep(1)
        print(self.instructions)
        sleep(0.5)
        print(self.how_to_close)
        sleep(0.5)
        print(self.salutation)
        sleep(0.25)
