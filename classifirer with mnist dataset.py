# -*- coding: utf-8 -*-
"""1 video numbers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1By0-P3b22CgQXXY7TevRx86xUgpvjQHc
"""

import tensorflow as tf

mnist=tf.keras.datasets.mnist

(x_train,y_train),(x_test,y_test)=mnist.load_data()

import matplotlib.pyplot as plt
plt.imshow(x_train[0],cmap=plt.cm.binary)

print(x_train[0].shape)

x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)

from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,  MaxPooling2D
model=Sequential()

model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dense(128,activation='relu'))
model.add(Dense(10,activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=3)

val_loss,val_acc=model.evaluate(x_test,y_test)
print(val_loss,val_acc)

predic=model.predict([x_test])

print(predic)

import numpy as np
print(np.argmax(predic[5]))

plt.imshow(x_test[5])