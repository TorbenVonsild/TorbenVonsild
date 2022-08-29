#Lav algoritme

#Import
import numpy as np
import pandas as pd
import os.path
import json
import matplotlib.pyplot as plt
import datetime as dt

#For Prediction
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Hent datasæt
aktieudvikling = pd.read_json("Data/aktieudvikling.json")
X = aktieudvikling.drop(columns=['udvikling_idag'])
y = aktieudvikling['udvikling_idag']

#For test slettes nederste linje - bruges som input data
X.drop(index=X.index[-1],axis=0,inplace=True)
y.drop(index=y.index[-1],axis=0,inplace=True)

# machinelearning
model = DecisionTreeRegressor()
model.fit(X, y)

#Hent forudsigelsesdata
#For test hentes seneste dag
prediction_data=aktieudvikling.iloc[[-1,]]
resultat = prediction_data.iloc[0,0]
prediction_data=prediction_data.drop(columns=['udvikling_idag'])

#Predict
forudsigelse = model.predict(prediction_data)
print("Stigningen forudsiges til ", forudsigelse, " men var ", resultat )

# verifikation:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model.fit(X_train, y_train)
forudsigelse = model.predict(X_test)


y=y_test.values.tolist()

mea = mean_absolute_error(y, forudsigelse)

print("Randomized nøjagtighed er ", mea)

# Plot the results
plt.figure()
plt.scatter(y, forudsigelse, s=20, edgecolor="black", c="darkorange", label="data")
#plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
#plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
#plt.axis([-0.06, 0.06, -0.06, 0.06])
plt.show()
