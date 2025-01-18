# Instantiate an object with a string of digits
# Method should have an integer as input
# Value error if the method input is longer than the digits string

# Algorithm
# Basically all possible substrings of the initial string

class Series:
    def __init__(self, digits):
        self.digits = digits

    def slices(self, series_length):
        if series_length > len(self.digits):
            raise ValueError
        
        return [[int(digit) for digit in self.digits[index: index + series_length]] 
                        for index in range(0, len(self.digits) - series_length + 1)]