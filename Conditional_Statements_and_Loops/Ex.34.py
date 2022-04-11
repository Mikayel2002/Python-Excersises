# Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20.

import sys

a = input("a = ")
b = input("b = ")

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
else:
    print("Wrong Value")
    sys.exit()

s = a + b

if 15 <= s <= 20:
    print(20)
else:
    print(s)


# with function
def summa(x, y):
    s = x + y
    if s in range(15, 20):
        return 20
    else:
        return s


print(summa(a, b))
