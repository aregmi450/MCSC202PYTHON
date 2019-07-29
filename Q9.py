# Write a program to calculate the sum of natural n natural numbers 1 + 2 + ⋯ + n.
# Calculate the sum when n = 10

import numpy as np

n=int(input())
print(np.sum(np.arange(1,n+1)))