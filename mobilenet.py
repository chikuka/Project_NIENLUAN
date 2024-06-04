import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os
import cv2
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import tensorflow as tf
from tensorflow import keras

# ========================duong dan======================================

# path="./vtho/"
# categories = ['BD_KT','DT_mu','vtho_1']

# path="./tay/"
# categories = ['BD_KT','DT_mu', 'tay_1', 'tay_2','tay_3']

# path="./chan/"
# categories = ['BD_KT', 'chan_1', 'chan_2','DT_mu']

path="./datasets/custom_data/images/"
categories = ['plastic','nylon','foam','other']

# path="./bung/"
# categories = ['BD_KT', 'bung_1', 'bung_2','bung_3','DT_mu']

# path="./toanthan/"
# categories = ['BD_KT','DT_mu','toanthan_1', 'toanthan_2','toanthan_3']

# path="./nhay/"
# categories = ['BD_KT','DT_mu', 'nhay_1', 'nhay_2']

# path="./dieuhoa/"
# categories = ['BD_KT', 'dieuhoa_1', 'dieuhoa_2','DT_mu']

# ==========================kiem tra anh dung thu muc khong====================================

# for category in categories:
#     fig, _ = plt.subplots(3,4)
#     fig.suptitle(category)
#     for k, v in enumerate(os.listdir(path+category)[:12]):
#         img = plt.imread(path+category+'/'+v)
#         plt.subplot(3, 4, k+1)
#         plt.axis('off')
#         plt.imshow(img)
#     plt.show()

# ==========================kich thuoc anh====================================

# shape0 = []
# shape1 = []

# for category in categories:
#     for files in os.listdir(path+category):
#         shape0.append(plt.imread(path+category+'/'+ files).shape[0])
#         shape1.append(plt.imread(path+category+'/'+ files).shape[1])
#     print(category, ' => height min : ', min(shape0), 'width min : ', min(shape1))
#     print(category, ' => height max : ', max(shape0), 'width max : ', max(shape1))
#     shape0 = []
#     shape1 = []

# =============================resize kich thuoc anh=================================

data = []#dữ liệu
labels = []#nhãn
imagePaths = []
HEIGHT = 64
WIDTH = 64
# 24 24
N_CHANNELS = 3

# ===========================lay ngau nhien anh===================================

for k, category in enumerate(categories):
    for f in os.listdir(path+category):
        imagePaths.append([path+category+'/'+f, k]) 

import random
random.shuffle(imagePaths)
print(imagePaths[:10])

# =======================tien xu ly=======================================

for imagePath in imagePaths:
    image = cv2.imread(imagePath[0])
    image = cv2.resize(image, (WIDTH, HEIGHT))  # .flatten()
    data.append(image)
    label = imagePath[1]
    labels.append(label)
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

plt.subplots(3,4)
for i in range(12):
    plt.subplot(3,4, i+1)
    plt.imshow(data[i])
    plt.axis('off')
    plt.title(categories[labels[i]])
# plt.show()

# ============================chia tap dl==================================

(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.2, random_state=42)# random_state=30)

trainY = np_utils.to_categorical(trainY, len(categories))

# //////////////////////////////MobileNet////////////////////////////////

EPOCHS = 20
INIT_LR = 1e-3
BS = 10
#--------------------------------------------
class_names = categories
#--------------------------------------------

from tensorflow.keras.applications import InceptionV3,MobileNet,VGG16,DenseNet121,EfficientNetB7#,DenseNet#EfficientNet
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from keras import layers
from keras import models


print("[INFO] compiling model...")
mobileNet = MobileNet(input_shape=(WIDTH, HEIGHT, N_CHANNELS), include_top=False, weights='imagenet')
for layer in mobileNet.layers:
    layer.trainable = False

model = Sequential()
model.add(mobileNet)
#model.add(layers.AveragePooling2D((8, 8), padding='valid', name='avg_pool'))
model.add(GlobalAveragePooling2D())
model.add(layers.Dropout(0.5))
model.add(layers.Flatten())
model.add(layers.Dense(len(class_names), activation='softmax'))

opt = tf.keras.optimizers.legacy.Adam(learning_rate=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
model.summary()

#Training
model.fit(trainX, trainY, batch_size=BS, epochs=EPOCHS, verbose=1)

# ----------------------------danh gia mo hinh---------------------------------
from numpy import argmax
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score

pred = model.predict(testX)
predictions = argmax(pred, axis=1) # return to label

cm = confusion_matrix(testY, predictions)

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Model confusion matrix')
fig.colorbar(cax)
ax.set_xticklabels([''] + categories)
ax.set_yticklabels([''] + categories)

for i in range(len(class_names)):
    for j in range(len(class_names)):
        ax.text(i, j, cm[j, i], va='center', ha='center')

plt.xlabel('Predicted')
plt.ylabel('True')
# plt.show()


accuracy = accuracy_score(testY, predictions)
print("Accuracy : %.2f%%" % (accuracy*100.0))
print("\n")
# ----------------------------------------------

recall= recall_score(testY, predictions,average='weighted')
print("Recall :%.2f%%" % (recall*100))
print("\n")
# ----------------------------------------------

precision = precision_score(testY, predictions,average='weighted')
print("Precision : %.2f%%" % (precision*100.0))
print("\n")
# ----------------------------------------------

f1 = f1_score(testY, predictions,average='weighted')
print("F1 : %.2f%%" % (f1*100.0))
print("\n")