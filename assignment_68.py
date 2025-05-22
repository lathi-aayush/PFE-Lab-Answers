# 68. Develop a Python program that counts the number of lines in a text file and displays the count.
with open("sample.txt", "r") as f:
    print(len(f.readlines()))
