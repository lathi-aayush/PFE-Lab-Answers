# 43. Program to insert and delete from dictionary

dictionary_example = {
    "apple": "a red or green fruit that is sweet and crunchy",
    "book": "a set of pages with stories or information",
    "cat": "a small animal that likes to chase mice",
    "run": "to move fast with your feet",
    "happy": "feeling good or joyful",
    "key": "value- pair",
}

# use the inbuilt operator .update({}) to insert in the dictionary
dictionary_example.update({"aayush": "FY student"})

# use the inbuilt operator .pop() to delete in the dictionary
dictionary_example.pop("happy")

print(dictionary_example)
