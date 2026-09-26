import pandas as pd

data = {
    "Sample": ["S1", "S2", "S3", "S4", "S5", "S6"],
    "Gene_A": [10, 15, 12, 25, 20, 18],
    "Gene_B": [14, 18, 16, 30, 22, 21],
    "Condition": ["Control", "Control", "Control", "Treated", "Treated", "Treated"]
}

df = pd.DataFrame(data)

s4_data = df.iloc[3]

print(s4_data)
