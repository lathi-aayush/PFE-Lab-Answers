# 37. Program to Generate Random Numbers from 1 to 20 and Append Them to the List 

import random

list_example = []

# creates 20 numbers in random order between the range of 1 to 20
for i in range (21):
    random_num = random.randrange(1, 21)
    
    # adding the random generated numbers to the list
    list_example.append(random_num)
    
print(f"The List of Generated Random numbers is : {list_example}")
    