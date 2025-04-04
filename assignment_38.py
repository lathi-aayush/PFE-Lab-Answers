# 38. Program to Remove the Duplicate Items from a List

list_example = []
list_new = []

print("Press 'Q' to quit : ")

while True:
    # Input any string in the list
    example = input("Enter any number in any order : ")

    # Making loop run until user enters q key to quit on will
    if example == 'q':
        break

    list_example.append(example)

for item in list_example:
    if item not in list_new:
        list_new.append(item)

print(f"The New list (without duplicates) is : {list_new}")
