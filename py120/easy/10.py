class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def __str__(self):
        return self.price

    def __lt__(self, other):
        if not isinstance(other, House):
            return NotImplemented
        
        return self.price < other.price

    def __gt__(self, other):
        if not isinstance(other, House):
            return NotImplemented
        
        return self.price > other.price
    
home1 = House(100000)
home2 = House(150000)
if home1 < home2:
    print("Home 1 is cheaper")
if home2 > home1:
    print("Home 2 is more expensive")