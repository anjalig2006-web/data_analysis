import pandas as pd

data = {
    "Sample": ["S1", "S2", "S3", "S4", "S5"],
    "Gene_A": [10, 12, 20, 22, 18],
    "Gene_B": [15, 18, 25, 30, 24],
    "Condition": ["Control", "Control", "Treated", "Treated", "Treated"]
}

df = pd.DataFrame(data)

sample_1 = df.sort_values("Gene_A")
print("Gene_A expression from lowest to highest: ",sample_1)

sample_2 = df.sort_values("Gene_B", ascending=False)
print("Gene_B expression from highest to lowest: ",sample_2)

sample_3 = df["Gene_A"].max()
print("Highest Gene_A expression: ",sample_3)
