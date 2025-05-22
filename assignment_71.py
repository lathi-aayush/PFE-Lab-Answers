# 71. Write a python program to create two 3X3 random matrixes and perform following operation: (a) Addition (b) subtraction (c) multiplication and display shape, dimensions, dtype, Rank and flatten output of every o/p matrix.
import numpy as np
a = np.random.randint(1, 10, (3, 3))
b = np.random.randint(1, 10, (3, 3))
print(a + b)
print(a - b)
print(a * b)
print((a + b).shape)
print((a + b).ndim)
print((a + b).dtype)
print((a + b).flatten())
