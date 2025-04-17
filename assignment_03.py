# 3. Program to Generate a Random Number

import time

seed = int(time.time())

print(seed);
rand_num = (seed % 100) + 1

print("Random number:", rand_num)

