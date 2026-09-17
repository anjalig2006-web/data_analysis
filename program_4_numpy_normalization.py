import numpy as np
expression = np.array([10, 20, 30, 40, 50])

minimum_value = np.min(expression)
print("Minimum expression value:",minimum_value)

maximum_value = np.max(expression)
print("Maximum expression value:",maximum_value)

normalized = (expression - minimum_value) / (maximum_value - minimum_value)
print ("Normalized expression values:", normalized)
