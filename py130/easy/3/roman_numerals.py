class RomanNumeral:
    ROMAN_MAPPING = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    def __init__(self, number):
        self.number = number

    def to_roman(self):
        roman_version = ""
        to_convert = self.number
        for key, value in RomanNumeral.ROMAN_MAPPING.items():
            multiplier, remainder = divmod(to_convert, value)
            if multiplier > 0:
                roman_version += key * multiplier
            to_convert = remainder
        return roman_version