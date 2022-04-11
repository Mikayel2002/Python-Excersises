# Write a Python program to count the number of even and odd numbers from a series of numbers.
import sys

n = input("Enter the number of elements in tuple: ")

if n.isdigit():
    n = int(n)
else:
    print("Wrong Value, 'n' must be integer type")
    sys.exit()

numbers = []

for i in range(n):
    numbers.append(int(input("Enter element: ")))

numbers = tuple(numbers)

odd_count = 0
even_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(numbers)
print("Count of even numbers {}".format(even_count))
print("Count of odd numbers {}".format(odd_count))
