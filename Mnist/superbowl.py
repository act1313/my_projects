from tensorflow import keras
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data = pd.read_csv("superbowl.csv")

data.drop(["SB", "Stadium", "MVP", "City", "State", "Date", "Loser", ], axis=1, inplace=True)

data = data.replace(["Kansas City Chiefs", "New England Patriots", "Philadelphia Eagles", "Denver Broncos"], [0, 1, 2, 3])
data = data.replace(["Seattle Seahawks", "Baltimore Ravens", "New York Giants", "Green Bay Packers"], [4, 5, 6, 7])
data = data.replace(["New Orleans Saints", "Pittsburgh Steelers", "Indianapolis Colts", "St. Louis Rams"], [8, 9, 10, 11])
data = data.replace(["Dallas Cowboys", "San Francisco 49ers", "Washington Redskins", "Chicago Bears"], [12, 13, 14, 15])
data = data.replace(["Los Angeles Raiders"], [16])
data = data.replace(["Oakland Raiders"], [16])
data = data.replace(["Miami Dolphins", "New York Jets"], [17, 18])
data = data.replace(["Baltimore Colts"], [10])
data = data.replace(["Tampa Bay Buccaneers"], [20])

x = data
y = data["Winner"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

model = keras.Sequential([
    keras.layers.Dense(128, activation="relu", input_dim=3),
    keras.layers.Dense(525, activation="relu"),
    keras.layers.Flatten(),
    keras.layers.Dense(10)
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(x_train, y_train, epochs=100)

prediction = model.predict(x_test)

test_loss, test_acc = model.evaluate(x_test, y_test)

print("Accuracy: ", test_acc)

print(prediction)
