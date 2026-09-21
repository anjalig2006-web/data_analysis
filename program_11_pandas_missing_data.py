import pandas as pd

import numpy as np

data = {
    "Sample": ["S1", "S2", "S3", "S4", "S5"],
    "Gene_A": [10, 12, np.nan, 22, 18],
    "Gene_B": [15, np.nan, 25, 30, 24],
    "Condition": ["Control", "Control", "Treated", "Treated", "Treated"]
}

df = pd.DataFrame(data)

missing = df.isnull()
print("Missing values in the DataFrame: ",missing)

missing_values_number = df.isnull().sum()
print("Number of missing values in each column: ",missing_values_number)

gene_A = df["Gene_A"].fillna(df["Gene_A"].mean())

gene_B = df["Gene_B"].fillna(df["Gene_B"].mean())

print("Final DataFrame:")
print(df)
