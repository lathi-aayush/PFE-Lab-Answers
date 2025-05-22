# 70. To keep record of patients’ medical data, manipulate files to store, update, and delete such information.
with open("patients.txt", "w") as f:
    f.write("Tom,Fever\nJerry,Cold")
with open("patients.txt", "a") as f:
    f.write("\nSpike,Cough")
with open("patients.txt", "r") as f:
    lines = f.readlines()
with open("patients.txt", "w") as f:
    for line in lines:
        if "Jerry" not in line:
            f.write(line)