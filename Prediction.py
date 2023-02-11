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

warnings.filterwarnings("ignore")

data = pd.read_csv("diabetes.csv")

y = data['Diabetes_binary'].values
X = data.drop(['Diabetes_binary'], 1).values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)


d_pred = log_reg.predict(X_test)

#print("Classification Report is:\n",classification_report(y_test,d_pred))


pickle.dump(log_reg, open('model.pkl', 'wb'))


model = pickle.load(open('model.pkl', 'rb'))
