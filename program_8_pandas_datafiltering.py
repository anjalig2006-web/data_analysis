import pandas as pd

data = {
    "Sample": ["S1", "S2", "S3", "S4", "S5"],
    "Gene_A": [10, 12, 20, 22, 18],
    "Gene_B": [15, 18, 25, 30, 24],
    "Condition": ["Control", "Control", "Treated", "Treated", "Treated"]
}

df = pd.DataFrame(data)

sample_1 = df[df["Gene_A"]>15]
print("The samples where Gene_A expression is greater than 15: ",sample_1)

sample_2 = df[df["Condition"] =="Treated"]
print("The samples belonging to the Treated condition: ",sample_2)

sample_3 = df[(df["Gene_A"]>15) & (df["Gene_B"]>25)]
print("The samples where Gene_A > 15 AND Gene_B > 25: ",sample_3)
