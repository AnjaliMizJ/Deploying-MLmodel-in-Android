# used platform is spider
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras


import numpy as np
import matplotlib.pyplot as plt


#loading the dataset
mnist = tf.keras.datasets.mnist
(images_train, labels_train),(images_test, labels_test) = mnist.load_data()

#specifying the classname
class_names = ["zero","one","two","three","four","five","six","seven","eight","nine"]

plt.figure()
plt.imshow(images_train[0])
plt.colorbar()
plt.grid(False)
plt.xlabel("Classification label: {}".format(labels_train[0]))
plt.show()


#normalizing the image data
images_train = images_train / 255.0
images_test = images_test / 255.0


#setting up the model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28,28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

#compiling and fitting the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(images_train, labels_train, epochs=16)

#evaluating the accuracy
test_loss, test_acc = model.evaluate(images_test, labels_test)
print('Test accuracy:', test_acc)



#saving the model using tflit in the specific location of the system
kearas_file = "digit.h5"
tf.keras.models.save_model(model,kearas_file)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tfmodel = converter.convert()
open("digit.tflite","wb").write(tfmodel)
