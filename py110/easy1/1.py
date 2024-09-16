# Write a program that solicits six (6) numbers from the user and prints a 
# message that describes whether the sixth number appears among the first five.

lst = []
for i in range(1, 6):
    number = input(f"Enter the {i}-th number: ")
    lst.append(number)

last = input("Enter the last number: ")

if last in lst:
    print(f"{last} is in {','.join(lst)}")
else:
    print(f"{last} isn't in {','.join(lst)}")