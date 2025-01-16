# Input: number
# Output: string (one of 3)
# Perfect: Aliquot sum = number
# Abundant: Aliquot sum > number
# Deficient: Aliquot sum < number

class PerfectNumber:
    PERFECT = 'perfect'
    ABUNDANT = 'abundant'
    DEFICIENT = 'deficient'

    @classmethod
    def classify(cls, number):
        if number <= 0:
            raise ValueError("Input must be a positive integer")
        
        sum_of_divisors = cls._find_sum_of_divisors(number)
        if sum_of_divisors == number:
            return PerfectNumber.PERFECT
        if sum_of_divisors > number:
            return PerfectNumber.ABUNDANT
        if sum_of_divisors < number:
            return PerfectNumber.DEFICIENT

    @staticmethod
    def _find_sum_of_divisors(number):
        sum_of_divisors = 0
        for candidate in range(1, number):
            if number % candidate == 0:
                sum_of_divisors += candidate
        return sum_of_divisors