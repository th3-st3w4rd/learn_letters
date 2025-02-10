from long_lists import alphabet, numbers, symbols


class GameContent:
    def __init__(self):
        self.active_modules = []
        self.__settings = self.get_setts()

        if "l" in self.__settings:
            self.__set_lower_case()

        if "L" in self.__settings:
            self.__set_upper_case()

        if "n" in self.__settings:
            self.__set_numbers()

        if "s" in self.__settings:
            self.__set_symbols()

    def get_setts(self):
        print("What would you like to work on?")
        print(
            "Enter one or all of the following letter, no need to add spaces or commas."
        )
        print("Enter 'l' for lower case letters...")
        print("Enter 'L' FOR UPPER CASE LETTERS...")
        print("Enter 'n' for numbers...")
        print("Enter 's' for symbols...")
        modules = input(
            "Insert the combination that you'd like to practice (l,L,n,s): "
        )
        return modules

    def __set_lower_case(self):
        self.active_modules.extend(alphabet)

    def __set_upper_case(self):
        for letter in alphabet:
            self.active_modules.extend(letter.upper())

    def __set_numbers(self):
        self.active_modules.extend(numbers)

    def __set_symbols(self):
        self.active_modules.extend(symbols)
