# 40. Program to create and view elements of a set

# defining a set
set_example = set()

print("Press 'Q' to quit : ")

while True:
    # Input any string in the list
    example = input("Enter any number in any order : ")

    # Making loop run until user enters q key to quit on will
    if example == "q":
        break

    set_example.add(example)

print(f"This set contains : {set_example}")
# output will not contain duplicate values