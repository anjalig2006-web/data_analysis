import pandas as pd

expression = pd.DataFrame({
    "Sample": ["S1", "S2", "S3", "S4"],
    "Gene_A": [10, 12, 20, 22],
    "Gene_B": [15, 18, 25, 30]
})

metadeta = pd.DataFrame({
    "Sample": ["S1", "S2", "S3", "S4"],
    "Age": [21, 25, 22, 24],
    "Condition": ["Control", "Control", "Treated", "Treated"]
})

merged_data = pd.merge(expression, metadeta, on="Sample")

condition_count = merged_data["Condition"].value_counts()
print(condition_count)
