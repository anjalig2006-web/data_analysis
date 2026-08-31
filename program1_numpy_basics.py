""" NumPy is a Python package used for numerical computing, especially for 
working with arrays and mathematical operations."""

import numpy as np

expression = np.array([12.4, 15.2, 8.7, 21.3, 17.6, 11.9, 25.4])

mean = np.mean (expression)
print("Mean gene expression:", mean)

maximum_value = np.max(expression)
print("Maximum expression:", maximum_value)

minimum_value = np.min(expression)
print("Minimum expression:", minimum_value)

above_mean = expression [expression > mean]
print("Values above mean:", above_mean)
