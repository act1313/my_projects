from tensorflow import keras as keras
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPool2D, Dropout
from tensorflow.keras.applications import VGG16
from tensorflow.keras.callbacks import EarlyStopping

train_path = "dataset/train"
test_path = "dataset/test"

size = 100
img_size = (size, size)
n_classes = 5

train_datagen = ImageDataGenerator(
    rescale=1./255,
	rotation_range=45,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest',
    validation_split=0.2
)

test_datagen = ImageDataGenerator(
    rescale=1./255
)

train = train_datagen.flow_from_directory(
    train_path,
    target_size=img_size,
    batch_size=64,
    seed=42,
    subset='training',
    shuffle=True,
    class_mode='categorical'
)

validation = train_datagen.flow_from_directory(
    train_path,
    target_size=img_size,
    batch_size=64,
    seed=42,
    subset='validation',
    shuffle=True,
    class_mode='categorical'
)

test = test_datagen.flow_from_directory(
    test_path,
    target_size=img_size,
    batch_size=64,
    seed=42,
    class_mode='categorical',
    shuffle=False
)

model = keras.Sequential()
conv_base = VGG16(include_top=False, input_shape=(size, size, 3))
conv_base.trainable = False

model.add(Conv2D(128, (1, 1), input_shape=(size, size, 3), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2), padding="same"))
model.add(Conv2D(256, (3, 3), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2), padding="same"))
model.add(Conv2D(256, (5, 5), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2), padding="same"))
model.add(Conv2D(256, (7, 7), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2), padding="same"))
"""
model.add(conv_base)
"""
model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dense(0.5))
model.add(Dense(5, activation="softmax"))

early_stop = EarlyStopping(monitor='val_loss', patience=2)

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(train, batch_size=16, epochs=25, verbose=1, validation_data=validation)


