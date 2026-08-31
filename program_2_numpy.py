import numpy as np

control = np.array ([10, 20, 8])
treated = np.array ([15, 12, 16])

difference = treated - control
print("Expression difference:", difference)

increased = difference > 0
decreased = difference < 0
print("Increased:", treated[difference > 0])
print("Decreased:", treated[difference < 0])

fold_change = treated / control
print("Fold change:", fold_change)
