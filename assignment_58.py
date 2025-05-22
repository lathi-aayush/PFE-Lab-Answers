# 58. Function to Find the Factorial of a Number Using Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
