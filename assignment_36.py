# 36. Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10

import math

list_example = []
list_output = []

print("Press '000' to quit : ")

while True:
    # Input any string in the list
    example = int(input("Enter any number in any order : "))

    # Making loop run until user enters q key to quit on will
    if example == 000:
        break

    list_example.append(example)

for i in range(len(list_example)):
    num = pow(list_example[i], 0.5)

    # program code for finding sum of digits
    n = list_example[i]
    sum_digits = 0
    m = n

    while m > 0:
        sum_digits += m % 10
        m = int(m / 10)

    if (num % int(num) == 0) and sum_digits < 10:
        list_output.append(list_example[i])

print(f"{list_output} is a list of perfect square whose sum of digits is less than 10")
