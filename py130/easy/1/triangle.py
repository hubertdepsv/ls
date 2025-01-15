class Triangle:
    EQUILATERAL = 'equilateral'
    ISOSCELES = 'isosceles'
    SCALENE = 'scalene'

    def __init__(self, a, b, c):
        if not self._is_valid(a, b, c):
            raise ValueError("Invalid triangle lengths")
        
        self.a = a
        self.b = b
        self.c = c

    @property
    def kind(self):
        if self.a == self.b == self.c:
            return Triangle.EQUILATERAL
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return Triangle.ISOSCELES
        return Triangle.SCALENE
    
    def _is_valid(self, a, b, c):
        return ((a > 0 or b > 0 or c > 0) and (
            (a < b + c) and (b < a + c) and (c < a + b)
        ))
    
