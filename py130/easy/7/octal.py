class Octal:
    BASE = 8
    VALID_DIGITS = "01234567"
    def __init__(self, string):
        self.string = string

    def to_decimal(self):
        if not self.__class__._valid_octal(self.string):
            return 0
        
        decimal_number = 0
        for index, digit in enumerate(self.string[::-1]):
            decimal_number += int(digit) * (self.__class__.BASE ** index)
        return decimal_number
    
    @staticmethod
    def _valid_octal(num):
        return all(char.isdigit() and "0" <= char <= "7" for char in num)