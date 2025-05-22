# 50. Program to Update the first set with items that don’t exist in the second set
s1 = {1, 2, 3}
s2 = {2, 3}
s1.difference_update(s2)
print(s1)