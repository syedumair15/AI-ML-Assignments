# 09_House_Price_Predictor.py
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([500,800,1000]).reshape(-1,1)
y = [100000,150000,200000]

model = LinearRegression()
model.fit(X,y)

print(model.predict([[900]]))
