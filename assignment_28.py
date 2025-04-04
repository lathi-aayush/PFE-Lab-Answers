# 28. Program to Create and view elements of a list

# initiating a list 
list_example = []

while True:
    # Input any string in the list
    example = input(("Enter anything you'd like to append in the list : "))
    list_example.append(example)
    
    # Making loop run until user enters q key to quit on will
    quit_key = input("\npress 'Q' key to quit : ")
    if quit_key.lower() == 'q':
        break
    

print(f"The contents of list are as follows : {list_example}")