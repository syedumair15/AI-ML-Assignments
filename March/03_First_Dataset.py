# 03_First_Dataset.py
import pandas as pd

data = {
    "Hours":[1,2,3,4,5],
    "Marks":[35,40,50,55,65]
}

df = pd.DataFrame(data)
print(df)
