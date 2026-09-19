import pandas as pd

data = {
    "Sample": ["S1", "S2", "S3", "S4", "S5"],
    "Gene_A": [10, 12, 20, 22, 18],
    "Gene_B": [15, 18, 25, 30, 24],
    "Condition": ["Control", "Control", "Treated", "Treated", "Treated"]
}

df = pd.DataFrame(data)
print("The complete DataFrame: ",df)

gene_A = df ["Gene_A"]
print ("Gene_A column: ",gene_A)

gene_B = df ["Gene_B"]
print ("Gene_B column: ",gene_B)

first_three = df.head(3)
print ("The first 3 rows are: ",first_three)
