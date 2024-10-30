def is_prime(list_of_primes, number):
    for prime in list_of_primes:
        if number % prime == 0:
            return False
    return True

def nearest_prime_sum(lst):
    lst_sum = sum(lst)
    primes = list(range(2, lst_sum + 1))
    for number in range(3, lst_sum + 1):
        # is number divisible by anything other than 1 or itself?
        for divisor in range(2, number):
            if number % divisor == 0 and divisor != number:
                primes.remove(number)
                break

    next_prime = lst_sum + 1
    while not is_prime(primes, next_prime):
        next_prime += 1
    
    return next_prime - lst_sum
    
    

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)