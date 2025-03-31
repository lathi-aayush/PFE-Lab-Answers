# 26. Program to display first n Fibonacci numbers

n = int(input("Enter any number : "))

f = [1, 1]

for i in range(n + 1):
    # f[i + 1] += f[i]
    s = f[i + 1] + f[i]
    f.append(s)

print(f"{n} Fibonacci is : {f}")

