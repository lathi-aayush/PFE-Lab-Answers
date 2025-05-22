# 45. Program to concatenate dictionaries to create a new one
d1 = {'a': 1}
d2 = {'b': 2}
d3 = {**d1, **d2}
print(d3)