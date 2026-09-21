import pandas as pd

data = {
    "Sample": ["S1", "S2", "S3", "S4", "S5"],
    "Gene_A": [10, 12, 20, 22, 18],
    "Gene_B": [15, 18, 25, 30, 24],
    "Condition": ["Control", "Control", "Treated", "Treated", "Treated"]
    }

df = pd.DataFrame(data)

grouped = df.groupby("Condition")

gene_A_mean = grouped["Gene_A"].mean()
print("The average Gene_A expression for each condition",gene_A_mean)

gene_B_mean = grouped["Gene_B"].mean()
print("The average Gene_B expression for each condition",gene_B_mean)
