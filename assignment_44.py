# 44. Program to sort (ascending and descending) a dictionary by value
 
d = {'a': 3, 'b': 1, 'c': 2}

def get_value(item):
    return item[1]

asc = dict(sorted(d.items(), key=get_value))
desc = dict(sorted(d.items(), key=get_value, reverse=True))

print(asc)
print(desc)
