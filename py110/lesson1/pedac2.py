# Imagine a sequence of consecutive even integers beginning with 2. The integers
# are grouped in rows, with the first row containing one integer, the second row
# two integers, the third row three integers and so on. Given an integer 
# representing the number of particular row, return an integer representing the
# sum of all the integers in that row.

# Problem
# 2
# 4 6
# 8 10 12
# 14 16 18 20
# Implicit: each row has the same number of numbers as its row number
# Data structure: list of lists
# Algorithm
# Create the row and then compute the sum
# To create the row we need to do all the rows before it
# for row 1 we start at 2
# for row 2 we take the next 2 even integers
# for row 3 we take the next 3 even integers etc

def consecutive(index):
    if index < 1:
        return 0
    
    rows = [[2]]
    for row_index in range(2, index + 1):
        row = [rows[-1][-1] + 2]
        element_index = 2
        while element_index <= row_index:
            row.append(row[-1] + 2)
            element_index += 1
        rows.append(row)
    return sum(rows[-1])

print(consecutive(1) == 2)
print(consecutive(2) == 10)
print(consecutive(4) == 68)