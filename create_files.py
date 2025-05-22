# Define the code for each question with the question as a comment
questions_code = {
    45: """# 45. Program to concatenate dictionaries to create a new one
d1 = {'a': 1}
d2 = {'b': 2}
d3 = {**d1, **d2}
print(d3)""",
    46: """# 46. Program to check whether a given key already exists in a dictionary.
d = {'a': 1, 'b': 2}
k = 'a'
print(k in d)""",
    47: """# 47. Program to merge two Python dictionaries
d1 = {'a': 1}
d2 = {'b': 2}
d1.update(d2)
print(d1)""",
    48: """# 48. Program to get the maximum and minimum value in a dictionary
d = {'a': 10, 'b': 5, 'c': 20}
print(max(d.values()))
print(min(d.values()))""",
    49: """# 49. Program to Add a list of elements to a set
s = {1, 2}
s.update([3, 4, 5])
print(s)""",
    50: """# 50. Program to Update the first set with items that don’t exist in the second set
s1 = {1, 2, 3}
s2 = {2, 3}
s1.difference_update(s2)
print(s1)""",
    51: """# 51. Program to Return a set of elements present in Set A or B, but not both
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)""",
    52: """# 52. Program to check if two sets have any elements in common.
a = {1, 2, 3}
b = {3, 4, 5}
print(not a.isdisjoint(b))""",
    53: """# 53. Program to Remove items from set1 that are not common to both set1 and set2
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1.intersection_update(s2)
print(s1)""",
    54: """# 54. Function to check if a number is even or odd
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
""",
    55: """# 55. Function to find the maximum of two numbers
def maximum(a, b):
    return a if a > b else b
""",
    56: """# 56. Function with keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=20, name='John')""",
    57: """# 57. Function with default arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")
""",
    58: """# 58. Function to Find the Factorial of a Number Using Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
""",
    59: """# 59. Function to Find the Sum of the Digits of the Number Recursively
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
""",
    60: """# 60. Create a function named count vowels that accepts a string and returns the number of vowels in the string.
def count_vowels(s):
    return sum(1 for c in s if c.lower() in 'aeiou')
""",
    61: """# 61. Write a function greet user that takes a user’s name as a parameter and prints a personalized greeting message.
def greet_user(name):
    print(f"Hello, {name}! Welcome back.")
""",
    62: """# 62. Given a sequence of integers that end with a 00. Print the sequence in reverse order. Don't use lists or other data structures. Use the force of recursion instead.
def reverse_input():
    n = int(input())
    if n == 0:
        return
    reverse_input()
    print(n)
""",
    63: """# 63. To keep record of students’ data, manipulate files to store, update, and delete students’ information.
with open("students.txt", "w") as f:
    f.write("John,21\\nAlice,22")
with open("students.txt", "a") as f:
    f.write("\\nBob,23")
with open("students.txt", "r") as f:
    lines = f.readlines()
with open("students.txt", "w") as f:
    for line in lines:
        if "Alice" not in line:
            f.write(line)""",
    64: """# 64. Write a Python program that reads the content of a text file and prints it to the console.
with open("sample.txt", "r") as f:
    print(f.read())
""",
    65: """# 65. Create a Python program that takes user input (a string) and writes it to a new text file.
text = input()
with open("newfile.txt", "w") as f:
    f.write(text)
""",
    66: """# 66. Write a Python program that reads a text file, counts the number of words in it, and writes the word count to a new file.
with open("sample.txt", "r") as f:
    count = len(f.read().split())
with open("count.txt", "w") as f:
    f.write(str(count))
""",
    67: """# 67. Write a Python program that reads the content of one text file and writes it to another file.
with open("source.txt", "r") as f1, open("dest.txt", "w") as f2:
    f2.write(f1.read())
""",
    68: """# 68. Develop a Python program that counts the number of lines in a text file and displays the count.
with open("sample.txt", "r") as f:
    print(len(f.readlines()))
""",
    69: """# 69. Write a Python program that appends a user-provided string to the end of an existing text file.
text = input()
with open("sample.txt", "a") as f:
    f.write("\\n" + text)
""",
    70: """# 70. To keep record of patients’ medical data, manipulate files to store, update, and delete such information.
with open("patients.txt", "w") as f:
    f.write("Tom,Fever\\nJerry,Cold")
with open("patients.txt", "a") as f:
    f.write("\\nSpike,Cough")
with open("patients.txt", "r") as f:
    lines = f.readlines()
with open("patients.txt", "w") as f:
    for line in lines:
        if "Jerry" not in line:
            f.write(line)""",
    71: """# 71. Write a python program to create two 3X3 random matrixes and perform following operation: (a) Addition (b) subtraction (c) multiplication and display shape, dimensions, dtype, Rank and flatten output of every o/p matrix.
import numpy as np
a = np.random.randint(1, 10, (3, 3))
b = np.random.randint(1, 10, (3, 3))
print(a + b)
print(a - b)
print(a * b)
print((a + b).shape)
print((a + b).ndim)
print((a + b).dtype)
print((a + b).flatten())
""",
    72: """# 72. Write a Python program to plot line chat, bar chart, pi chart, scatter chart, histogram for taking two different arrays as input.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x, y)
plt.show()
plt.bar(x, y)
plt.show()
plt.pie(y, labels=x)
plt.show()
plt.scatter(x, y)
plt.show()
plt.hist(y)
plt.show()
"""
}

# Create or overwrite individual files for each question
for q_num, code in questions_code.items():
    file_name = f"assignment_{q_num}.py"
    with open(file_name, "w") as file:
        file.write(code)

print("Files created/overwritten successfully!")
