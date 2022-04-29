# Write a Python program to find the numbers that are greater than
# 10 and have odd first and last digits.
import sys

n = input("Enter the number of elements in tuple: ")

if n.isdigit():
    n = int(n)
else:
    print("Wrong Value, 'n' must be integer type")
    sys.exit()

numbers = []

for i in range(n):
    numbers.append(int(input("Enter the element: ")))

for x in numbers:
    if x > 10 and int(str(x)[0]) % 2 == 1 and int(str(x)[-1]) % 2 == 1:
        print(x, end=" ")
