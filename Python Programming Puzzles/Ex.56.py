# Write a Python program to find an integer exponent x such that a^x = n.

def test(a, n):
    m = 1
    x = 0
    while m != n:
        x += 1
        m *= a

    return x


a = int(input("a = "))
n = int(input("n = "))

print(test(a, n))
