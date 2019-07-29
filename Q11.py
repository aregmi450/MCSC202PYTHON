# Write a program to find the smallest integer n such that 3 n ≥ 2000
import numpy as np
print(np.ceil(np.log(2000) / np.log(3)))