#  Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note:
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

import sys

a = input("a = ")
b = input("b = ")
c = input("c = ")

if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)
else:
    print("Wrong Value")
    sys.exit()


def triangle_check(x, y, z):
    if x == y == z:
        return "The triangle is equilateral"
    elif x == y or y == z or z == x:
        return "The triangle is isosceles"
    else:
        return "The triangle is scalene"


print(triangle_check(a, b, c))
