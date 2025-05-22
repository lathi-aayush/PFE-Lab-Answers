# 59. Function to Find the Sum of the Digits of the Number Recursively
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
