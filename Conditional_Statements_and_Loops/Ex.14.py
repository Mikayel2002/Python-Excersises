# Write a Python program that accepts a string and calculate the number of digits and letters.


str1 = input("Enter the string: ")

letter_count = 0
digit_count = 0

for i in str1:
    if i.isdigit():
        digit_count += 1
    if i.isalpha():
        letter_count += 1

print("Count of letters in string: {}".format(letter_count))
print("Count of digits in string {}".format(digit_count))
