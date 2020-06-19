import numpy as np
import pandas as pd
import sklearn
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

y = train_data["Survived"]

train_data.replace("female", 0)
train_data.replace("male", 1)

whatIwant = ["Pclass", "Sex", "SibSp", "Parch"]

X = pd.get_dummies(train_data[whatIwant])
X_test = pd.get_dummies(test_data[whatIwant])

model = KNeighborsClassifier(n_neighbors=2)
model.fit(X, y)

prediction = model.predict(X_test)

final = pd.DataFrame({"PassengerId": test_data.PassengerId, "Survived": prediction})

final.to_csv("my_submission.csv", index=False)
print("It worked!")
