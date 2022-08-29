import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Hent datasæt
kurser_data = pd.read_excel('novoexcell.xlsx')
X = kurser_data.drop(columns=['today'])
y = kurser_data.drop(columns=['turnover', 'before', 'night', 'omx'])

# verifikation:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# machinelearning
model = DecisionTreeClassifier()
model.fit(X, y)

# verification
model.fit(X_train, y_train)
forudsigelse = model.predict(X_test)
score = accuracy_score(y_test, forudsigelse)
print (score)