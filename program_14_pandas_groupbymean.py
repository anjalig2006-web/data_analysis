import pandas as pd

data = {
    "Sample": ["S1", "S2", "S3", "S4", "S5", "S6"],
    "Gene_A": [10, 12, 20, 22, 18, 25],
    "Gene_B": [15, 18, 25, 30, 24, 28],
    "Condition": ["Control", "Control", "Control", "Treated", "Treated", "Treated"]
}

df = pd.DataFrame(data)

print(df)

grouped = df.groupby("Condition")

gene_A_mean = grouped["Gene_A"].mean()
print(gene_A_mean)
