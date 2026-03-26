# 11_Customer_Segmentation.py
from sklearn.cluster import KMeans
import pandas as pd

data = {"Income":[20,30,40,50],"Score":[30,60,70,90]}
df = pd.DataFrame(data)

k = KMeans(n_clusters=2)
df["Cluster"] = k.fit_predict(df)

print(df)
