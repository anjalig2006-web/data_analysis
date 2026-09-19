import numpy as np

expression = np.array ([[10, 12, 15, 18], [20, 22, 19, 25], [5,  8,  10, 12]])

shape = np.shape(expression)
print ("The shape of the expression dataset: ", shape)

gene_1 = expression [0]
print("Gene 1 expression:",gene_1)

sample_1 = expression [:,1]
print("Sample 1 expression:",sample_1)

gene_means = np.mean(expression, axis=1)
print("Mean expression of each gene:",gene_means)
