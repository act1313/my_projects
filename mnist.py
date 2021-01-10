import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from tensorflow.keras.applications import VGG16
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

y_cat_train = to_categorical(y_train, 10)
y_cat_test = to_categorical(y_test, 10)

x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

import tensorflow.keras as keras
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from tensorflow.keras.applications import VGG16

model = keras.Sequential()

# CONVOLUTIONAL LAYER
model.add(Conv2D(filters=32, kernel_size=(4, 4),
                 input_shape=(28, 28, 1), activation='relu',))
# POOLING LAYER
model.add(MaxPool2D(pool_size=(2, 2), padding="same"))
model.add(Conv2D(filters=32, kernel_size=(4, 4),
                 input_shape=(28, 28, 1), activation="relu"))
model.add(MaxPool2D(pool_size=(2, 2), padding="same"))
model.add(Conv2D(filters=32, kernel_size=(4, 4),
                 input_shape=(28, 28, 1), activation="relu"))
model.add(MaxPool2D(pool_size=(2, 2), padding="same"))
# FLATTEN IMAGES FROM 28 by 28 to 764 BEFORE FINAL LAYER
model.add(Flatten())

# 128 NEURONS IN DENSE HIDDEN LAYER (YOU CAN CHANGE THIS NUMBER OF NEURONS)
model.add(Dense(128, activation='relu'))

# LAST LAYER IS THE CLASSIFIER, THUS 10 POSSIBLE CLASSES
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_cat_train, epochs=100, validation_data=(x_test, y_cat_test))
