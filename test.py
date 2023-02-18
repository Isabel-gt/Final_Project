import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model('my_model')


x_new = np.array([0, 1, 1, 0, 1, 0, 1, 0, 0, 1])

x_2d = x_new.reshape(1, -1)

y_new = model.predict(x_2d)


print("Predicted value:", y_new)