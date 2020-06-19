import pandas as pd
import numpy as np
from tensorflow import keras

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

y = train_data["Survived"]

train_data.replace("female", 0)
train_data.replace("male", 1)
test_data.replace("female", 0)
test_data.replace("male", 1)
whatIwant = ["Pclass", "Sex", "SibSp", "Parch"]

X = pd.get_dummies(train_data[whatIwant])
X_test = pd.get_dummies(test_data[whatIwant])
X = np.array(X)
X_test = np.array(X_test)
y = np.array(y)
X = X.reshape(4455)
y = y.reshape(891)
X_test = X_test.reshape(2090)

test_data["A_Class"] = 0
test_data["B_Class"] = 0
test_data["C_Class"] = 0

test_data.loc[test_data.Pclass == 1, "A_Class"] = 1

input_shape = -1

model = keras.Sequential([
    keras.layers.Dense(128, input_shape=[4455, 1], activation="relu"),
    keras.layers.Dense(525, activation="relu"),
    keras.layers.Flatten(),
    keras.layers.Dense(10)
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(X, y, batch_size=16, epochs=5)

prediction = model.predict(X_test)

final = pd.DataFrame({"PassengerId": test_data["PassengerId"], "Survived": prediction})

final.to_csv("my_submission.csv", index=False)
print("It worked!")
