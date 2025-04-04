# 30. Program to access List Index and Values

list_example = [
    "curiosity",
    "startup energy",
    "AI enthusiasm",
    "philosophical depth",
    "experimental spirit",
]

i = int(
    input(
        "Between 1 to 5 ,enter any number which you would like to access in this list : "
    )
)

if i > 0 and i < 6:
    print(f"Index '{i}' has '{list_example[i-1]}'")
    print(f"This is the original list : {list_example}")
else:
    print("Please enter between 1 to 5")
