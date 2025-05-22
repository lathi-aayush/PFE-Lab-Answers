# 60. Create a function named count vowels that accepts a string and returns the number of vowels in the string.
def count_vowels(s):
    return sum(1 for c in s if c.lower() in 'aeiou')
