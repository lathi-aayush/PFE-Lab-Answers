# 22. Program to display numbers in the reverse order

n = int(input("Enter any number : "))
list_n = []

for i in range(1, n + 1):
    list_n.append(i)

list_n.reverse()

print(f"In reversed : {list_n}")
