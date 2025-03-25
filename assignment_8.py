# 8. A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased. The program should read three integers: the number of students in each of the three classes, a, b and c respectively. In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks is also enough for the third group of 22 students. So we need 32 desks in total.

class1 = int(input("Enter the Number of students in class 1 : "))
class2 = int(input("Enter the Number of students in class 2 : "))
class3 = int(input("Enter the Number of students in class 3 : "))

table1 = (class1//2) + (class1%2)   
table2 = (class2//2) + (class2%2)   
table3 = (class3//2) + (class3%2)   

print(f"Minimum desks in class 1 is {table1}")
print(f"Minimum desks in class 2 is {table2}")
print(f"Minimum desks in class 3 is {table3}")

print("Total Number of Desks required is : ", table1 + table2 + table3)
