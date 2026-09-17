import numpy as np

gene_A = np.array([10, 20, 30, 40, 50])
gene_B = np.array([12, 24, 29, 42, 48])

correlation_coefficient = np.corrcoef(gene_A, gene_B)[0, 1]
print ("The correlation coefficient between Gene A and Gene B: ",correlation_coefficient)

if correlation_coefficient > 0:
    print("The genes have a positive correlation.")
elif correlation_coefficient < 0:
    print("The genes have a negative correlation.")
else:
    print("The genes have no correlation.")
