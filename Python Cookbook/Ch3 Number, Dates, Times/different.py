# Calculating with Large Numerical Arrays
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

a = x * 2  # [1, 2, 3, 4, 1, 2, 3, 4]
# b = x + 10  # Error
c = x + y  # [1, 2, 3, 4, 5, 6, 7, 8]

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])

ax * 2  # array([2, 4, 6, 8])
ax + 10  # array([11, 12, 13, 14])
ax * ay  # array([5, 12, 21, 32])
