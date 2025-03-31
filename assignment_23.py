# 23. Program to check if a number is prime

n = int(input("Enter number to check for prime: "))

for i in range(2, n):
    if n % i != 0:
        c = 1
    else:
        # c = 'not_prime'
        c = 0
        break

if c == 1:
    print(f"The Number {n} is prime")
elif c == 0:
    print(f"{n} is not prime")
