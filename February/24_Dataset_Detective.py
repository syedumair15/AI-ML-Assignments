# 24_Dataset_Detective.py
import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())

num = df.select_dtypes(include="number")
print(num.mean().idxmax())

print(df.isnull().sum())
