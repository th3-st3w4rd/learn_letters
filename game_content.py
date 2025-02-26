from long_lists import alphabet, numbers, symbols


class GameContent:
    def __init__(self, *args):
        self.active_modules = []
        self.args = args[0]

        if self.args.lower_letters:
            self.__set_lower_case()
        
        if self.args.upper_letters:
            self.__set_upper_case()

        if self.args.numbers:
            self.__set_numbers()

        if self.args.symbols:
            self.__set_symbols()

    def __set_lower_case(self):
        self.active_modules.extend(alphabet)

    def __set_upper_case(self):
        for letter in alphabet:
            self.active_modules.extend(letter.upper())

    def __set_numbers(self):
        self.active_modules.extend(numbers)

    def __set_symbols(self):
        self.active_modules.extend(symbols)
