# Write a Python program to print the even numbers from a given list.

import sys

n = input("Enter the number of elements in tuple: ")

if n.isdigit():
    n = int(n)
else:
    print("Wrong Value, 'n' must be integer type")
    sys.exit()

numbers = []
new_list = []

for i in range(n):
    numbers.append(int(input("Enter the elements: ")))


def even_numbers(numbers_1):
    for x in numbers_1:
        if x % 2 == 0:
            new_list.append(x)

    return new_list


print(even_numbers(numbers))
