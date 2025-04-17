# 3. Program to Generate a Random Number

import time

# Get the current time in seconds (as a float), then convert to int for a seed
seed = int(time.time())

# Generate a pseudo-random number based on the seed
print(seed);
rand_num = (seed % 100) + 1

# Display the random number
print("Random number:", rand_num)

