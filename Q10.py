# Write a program to calculate the sum of squares of natural n natural numbers 1 2 + 2 2 +
# ⋯ + n 2 . Calculate the sum when n = 5.

import numpy as np

n=int(input())
print(np.sum(np.arange(1,n+1) ** 2))