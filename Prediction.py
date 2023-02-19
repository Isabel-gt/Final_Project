import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
from sklearn import metrics
import warnings
import pickle
import math
import joblib

warnings.filterwarnings("ignore")

data = pd.read_csv("diabetes.csv")

y = data['Diabetes_binary'].values
X = data.drop(['Diabetes_binary', 'Age', 'GenHlth',
               'HighBP',
               'BMI',
               'PhysActivity',
               'PhysHlth',
               'DiffWalk',
               'HeartDiseaseorAttack',
               'Fruits',
               'Stroke',
               'AnyHealthcare',
               'Smoker',
               'Veggies',
               'HvyAlcoholConsump',
               'HighChol'], 1).values

X = X.astype('int')
y = y.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)
print(X_train)
log_reg = LogisticRegression()
#log_reg.fit(X_train, y_train)

fit_log_reg = log_reg.fit(X_train, y_train)
intercept = fit_log_reg.intercept_
coefficient = fit_log_reg.coef_
new_list = [intercept, coefficient]
print(new_list)
print(len(intercept))
print(len(coefficient))
d_pred = log_reg.predict(X_test)

#print("Classification Report is:\n",classification_report(y_test,d_pred))


joblib.dump(log_reg, open('model.pkl', 'wb'))


model = joblib.load(open('model.pkl', 'rb'))
