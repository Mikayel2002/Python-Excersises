# Write a Python function to create and print a list where
# the values are square of numbers between 1 and 30 (both included).

def square_of_numbers_in_list():
    list_1 = []
    for i in range(1, 31):
        list_1.append(i ** 2)

    print(list_1)


square_of_numbers_in_list()
