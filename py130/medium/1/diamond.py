class Diamond:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    @staticmethod
    def make_diamond(letter):
        letter_index = Diamond.ALPHABET.index(letter)
        letter_diamond = ""
        # create each line
        letter_diamond += f"{(letter_index)* ' '}{Diamond.ALPHABET[0]}{letter_index * ' '}\n"
        for index in range(1, letter_index + 1):
            letter_diamond += f"{(letter_index - index) * ' '}{Diamond.ALPHABET[index]}{(2 * index - 1) * ' '}{Diamond.ALPHABET[index]}{(letter_index - index) * ' '}\n"
        # 2nd half of the diamond
        for index in range(letter_index - 1, 0, -1):
            letter_diamond += f"{(letter_index - index) * ' '}{Diamond.ALPHABET[index]}{(2 * index - 1) * ' '}{Diamond.ALPHABET[index]}{(letter_index - index) * ' '}\n"
        if letter_index != 0:
            letter_diamond += f"{(letter_index)* ' '}{Diamond.ALPHABET[0]}{letter_index * ' '}\n"

        return letter_diamond