from datetime import date
# datetime.date(2024, 1, 13).weekday()

def friday_the_13ths(year):
    count = 0
    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            count += 1
    return count

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True