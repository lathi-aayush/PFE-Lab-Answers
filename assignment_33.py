# 33. Program to Find the Largest Number in a List

list_example = []

print("Press '000' to quit : ")

while True:
    # Input any string in the list
    example = int(input("Enter any number in any order : "))
    list_example.append(example)

    # Making loop run until user enters q key to quit on will
    if example == 000:
        break

# sorting in ascending order
list_example.sort()
# reversing the list to get the descending order
list_example.reverse()

print(f"The list is : {list_example}")
print(f"\nThe Largest number of the list is : {list_example[0]}")
