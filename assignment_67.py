# 67. Write a Python program that reads the content of one text file and writes it to another file.
with open("source.txt", "r") as f1, open("dest.txt", "w") as f2:
    f2.write(f1.read())
