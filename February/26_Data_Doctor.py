# 26_Data_Doctor.py
import pandas as pd

df = pd.read_csv("dataset.csv")

df.fillna(df.mean(numeric_only=True), inplace=True)
df.fillna("unknown", inplace=True)

df.drop_duplicates(inplace=True)

for col in df.select_dtypes(include="object"):
    df[col] = df[col].str.lower().str.strip()

print(df.head())
