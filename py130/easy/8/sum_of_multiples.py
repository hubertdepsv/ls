# sum of all multiples of the numbers in the set that are less than the 1st number
# e.g. multiples of 3 and 5 less than 20 = 78

# initialise an empty array of multiples
# for each number in the input list
# for i in range(max // number):
#    multiples.append(number * i)
# get the set of multiples, sum it and return

# what should we do if there is only a maximum? use 3 and 5 as a default set

class SumOfMultiples:
    def __init__(self, *args):
        self.multiples = args if args else (3, 5)
    
    def to(self, num):
        return sum(x for x in range(1, num) if self._any_multiple(x))
    
    @classmethod
    def sum_up_to(cls, num):
        return cls().to(num)
    
    def _any_multiple(self, num):
        return any(num % multiple == 0 for multiple in self.multiples)