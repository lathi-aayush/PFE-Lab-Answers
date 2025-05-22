# 66. Write a Python program that reads a text file, counts the number of words in it, and writes the word count to a new file.
with open("sample.txt", "r") as f:
    count = len(f.read().split())
with open("count.txt", "w") as f:
    f.write(str(count))
