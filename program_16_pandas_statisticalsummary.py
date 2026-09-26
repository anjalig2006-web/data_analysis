import pandas as pd

data = {
    "Sample": ["S1", "S2", "S3", "S4", "S5", "S6"],
    "Gene_A": [10, 15, 12, 25, 20, 18],
    "Condition": ["Control", "Control", "Control", "Treated", "Treated", "Treated"]
}

df = pd.DataFrame(data)

print(df)

summary = df["Gene_A"].describe()

print(summary)
