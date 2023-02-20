import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score,accuracy_score
from joblib import dump
import pickle

file_path = ('diabetes.csv')
df = pd.read_csv(file_path)

catcol = ['HighBP', 'CholCheck','BMI',
       'Smoker', 'Stroke', 'PhysActivity','NoDocbcCost', 'Sex','Age', 'Education']

new_df = df[catcol]
new_df.head()

y = df['Diabetes_binary'].values
X = new_df.values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)

reg = LogisticRegression(max_iter=1000000)

reg.fit(X_train,y_train)

pickle.dump(reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))