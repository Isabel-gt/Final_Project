import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import warnings
import pickle
import math

warnings.filterwarnings("ignore")

data = pd.read_csv("diabetes.csv")

y = data['Diabetes_binary'].values
X = data.drop(['Diabetes_binary'], 1).values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)

d_model = RandomForestClassifier(n_estimators=1000)
d_model.fit(X_train, y_train)

nd_pred = d_model.predict(X_test)

#print("Classification Report is:\n",classification_report(y_test,d_pred))


pickle.dump(nd_pred, open('model2.pkl', 'wb'))


model2 = pickle.load(open('model2.pkl', 'rb'))
