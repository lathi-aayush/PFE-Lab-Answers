# 24. Program to calculate sum and average of first n numbers

n = int(input("Enter any number : "))
sum_n = 0

for i in range(1, n + 1):
    sum_n = sum_n + i

avg = sum_n / n
print(f"For the first {n} Numbers\nThe Sum is : {sum_n} and Average is : {avg}")
