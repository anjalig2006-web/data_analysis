import numpy as np
expression = np.array([12, 15, 18, 10, 20, 15])

mean = np.mean(expression)
print ("Mean gene expression: ",mean)

median = np.median(expression)
print ("Median gene expression: ",median)

standard_deviation = np.std(expression)
print ("Standard deviation of the expression values: ", standard_deviation)

above_mean = expression [expression > mean]
print ("Expression values that are above the mean: ",above_mean)
