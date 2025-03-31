# 25. Program to display first n multiples of a number

n = int(input("Enter any number : "))
multi = int(input("Enter any number : "))

for i in range(multi):
    print((i + 1) * n, end=" ")
