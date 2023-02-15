import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
#import tensorflow as tf
from sklearn import metrics
import warnings
import pickle
import math

warnings.filterwarnings("ignore")

data = pd.read_csv("diabetes.csv")

y = data['Diabetes_binary'].values
X = data.drop(['Diabetes_binary'], 1).values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)

#scaler = StandardScaler()


#X_scaler = scaler.fit(X_train)


#X_train_scaled = X_scaler.transform(X_train)
#X_test_scaled = X_scaler.transform(X_test)


#number_input_features = len(X_train[0])
#hidden_nodes_layer1 = 80
#hidden_nodes_layer2 = 30
#hidden_nodes_layer3 = 30
hidden_nodes_layer4 = 30
##hidden_nodes_layer5 = 30

#nn = tf.keras.models.Sequential()

# nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer1,
# input_dim=number_input_features, activation="relu"))

#nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer2, activation="relu"))

#nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer3, activation="relu"))

#nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer4, activation="relu"))

#nn.add(tf.keras.layers.Dense(units=hidden_nodes_layer5, activation="relu"))

#nn.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

# nn.summary()

#nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

#fit_model = nn.fit(X_train, y_train, epochs=30)

#model_loss, model_accuracy = nn.evaluate(X_test_scaled, y_test, verbose=2)


#pickle.dump(model_accuracy, open('model1.pkl', 'wb'))


#model1 = pickle.load(open('model1.pkl', 'rb'))
