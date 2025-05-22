# 69. Write a Python program that appends a user-provided string to the end of an existing text file.
text = input()
with open("sample.txt", "a") as f:
    f.write("\n" + text)
