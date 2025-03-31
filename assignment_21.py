# 21. Program to calculate factorial of a numbers

# 5! = 5*4*3*2*1

n = int(input("Enter any number : "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"Factorial of {n}! is {fact}")
