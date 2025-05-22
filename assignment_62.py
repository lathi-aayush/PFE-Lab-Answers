# 62. Given a sequence of integers that end with a 00. Print the sequence in reverse order. Don't use lists or other data structures. Use the force of recursion instead.
def reverse_input():
    n = int(input())
    if n == 0:
        return
    reverse_input()
    print(n)
