# 63. To keep record of studentsí data, manipulate files to store, update, and delete studentsí information.
with open("students.txt", "w") as f:
    f.write("John,21\nAlice,22")
with open("students.txt", "a") as f:
    f.write("\nBob,23")
with open("students.txt", "r") as f:
    lines = f.readlines()
with open("students.txt", "w") as f:
    for line in lines:
        if "Alice" not in line:
            f.write(line)