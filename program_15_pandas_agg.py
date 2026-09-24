import pandas as pd

data = {
    "Sample": ["S1", "S2", "S3", "S4", "S5", "S6"],
    "Gene_A": [8, 12, 16, 20, 24, 28],
    "Condition": ["Control", "Control", "Control", "Treated", "Treated", "Treated"]
}

df = pd.DataFrame(data)

print(df)

grouped = df.groupby("Condition")

gene_A_summary = grouped["Gene_A"].agg(["mean", "max", "min"])

print(gene_A_summary)
