import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import os

# get data
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

X_train = train.drop(labels=["label"], axis=1)
y_train = train["label"]

X_test = test

# preprocess data
X_train = X_train / 255.0
X_test = X_test / 255.0

X_train = X_train.values.reshape(-1, 28, 28, 1)
X_test = X_test.values.reshape(-1, 28, 28, 1)

X_train = np.asarray(X_train)
X_test = np.asarray(X_test)
y_train = np.asarray(y_train)

# get more memory
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)

# make a model
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), padding="Same", activation="relu", input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Conv2D(64, (3, 3), padding="Same", activation="relu"),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Conv2D(128, (1, 1), padding="Same", activation="relu"),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Flatten(input_shape=(28, 28, 1)),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# train the model
model.fit(X_train, y_train, epochs=5, batch_size=2)

# predict
prediction = model.predict(X_test)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

prediction = np.argmax(prediction, axis=1)

results = pd.Series(prediction, name="Label")
submission = pd.concat([pd.Series(range(1, 28001), name="ImageId"), results], axis=1)

submission.to_csv("submission2.csv", index=False)
