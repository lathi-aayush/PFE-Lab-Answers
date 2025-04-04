# 35. Program to Put Even and Odd elements in a List into Two Different Lists

list_example = []
list_even = []
list_odd = []

print("Press '000' to quit : ")

while True:
    # Input any string in the list
    example = int(input("Enter any number in any order : "))

    # Making loop run until user enters q key to quit on will
    if example == 000:
        break

    list_example.append(example)


for i in range(len(list_example)):
    if list_example[i] % 2 == 0:
        list_even.append(list_example[i])
    else:
        list_odd.append(list_example[i])

list_even.sort()
list_odd.sort()

print(f"The Unsorted list is {list_example}")
print(f"\nThe Even sorted list is {list_even}")
print(f"The Odd sorted list is {list_odd}")
