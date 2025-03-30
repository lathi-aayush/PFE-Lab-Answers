# 16. Given a string. Delete from it all the characters whose indices are divisible by 3

word = input("Enter any word : ")
new_word = word[0]


for i in range(0, len(word)):
    if i % 3 != 0:
        new_word += word[i]

print(f"After processing the word '{word}' it becomes '{new_word}'")
