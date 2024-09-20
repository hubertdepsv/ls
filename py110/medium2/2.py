def triangle(side1, side2, side3):
    sides = sorted([side1, side2, side3])
    if (min(sides) < 0) or (sides[-1] > (sides[0] + sides[0])):
        return "invalid"
    if side1 == side2 == side3:
        return "equilateral"
    if side1 == side2 or side2 == side3 or side1 == side3:
        return "isosceles"
    return "scalene"
    
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
print(triangle(3, 1, -1) == "invalid")     # True