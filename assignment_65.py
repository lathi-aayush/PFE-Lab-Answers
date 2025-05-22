# 65. Create a Python program that takes user input (a string) and writes it to a new text file.
text = input()
with open("newfile.txt", "w") as f:
    f.write(text)
