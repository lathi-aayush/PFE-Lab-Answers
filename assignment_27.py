# 27. Program to find the sum of digits of a number 

n = int(input("Enter any number : "))

sum_digits = 0
m= n

while m>0:
    sum_digits += m%10
    m = int(m/10)

print(f"Sum of Digits of {n} is {sum_digits}")   

    