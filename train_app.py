import pandas as pd
from pathlib import Path
import plotly.express as px
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder
import tensorflow as tf

file_path = ('diabetes.csv')
df = pd.read_csv(file_path)

catcol = ['HighBP', 'CholCheck','BMI',
       'Smoker', 'Stroke', 'PhysActivity','NoDocbcCost', 'Sex','Age', 'Education']

new_df = df[catcol]
new_df.head()

y = df['Diabetes_binary'].values
X = new_df.values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)

scaler = StandardScaler()

X_scaler = scaler.fit(X_train)

X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

number_input_features = len(X_train[0])
hidden_nodes_layer1 = 80
hidden_nodes_layer2 = 30
hidden_nodes_layer3 = 30


model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=hidden_nodes_layer1, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(units=hidden_nodes_layer2, activation='relu'),
    tf.keras.layers.Dense(units=hidden_nodes_layer3, activation='relu'),
    tf.keras.layers.Dense(units=1, activation="sigmoid")
])

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X_train, y_train, epochs=10, batch_size=32)

model.save('my_model')