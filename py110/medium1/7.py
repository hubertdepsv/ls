def fibonacci(number):
    if (number == 1) or (number == 2):
        return 1
    fibonacci_sequence = [1, 1]
    for n in range(2, number):
        fibonacci_sequence.append(fibonacci_sequence[n-1] + fibonacci_sequence[n-2])
    return fibonacci_sequence[-1]


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True