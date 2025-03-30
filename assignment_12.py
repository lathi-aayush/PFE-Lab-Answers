# 12. Program to find maximum of three numbers

x = int(input(f"Enter 1st Number : "))
y = int(input(f"Enter 2nd Number : "))
z = int(input(f"Enter 3rd Number : "))

# You cannot use this because this is an assignment on operators
# print(max(x, y, z))

if x >= y and x >= z:
    print("1st Num is the greatest")
elif y >= x and y >= z:
    print("2nd Num is the greatest")
elif z >= x and z >= y:
    print("3rd Num is the greatest")
