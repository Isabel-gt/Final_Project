
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
##from imblearn.ensemble import BalancedRandomForestClassifier
#from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics
#import tensorflow as tf
from pathlib import Path
import pandas as pd
import numpy as np
import warnings
import math
import pickle
import joblib
from flask import Flask, jsonify, redirect, url_for, render_template, request

app = Flask(__name__)


model = joblib.load(open('model.pkl', 'rb'))
Xscaler = joblib.load(open('Xscaler.pkl', 'rb'))


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@ app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        result = request.form.getlist('validate')
        num_features = [[int(x) for x in result]]
        my_list_sample = Xscaler.transform(np.asarray(num_features))
        diabetesPredict = model.predict(my_list_sample)
        diabetesProbability = model.predict_proba(my_list_sample)

    if diabetesPredict[0] == 1:

        return "Patient diagnosis is diabetic. \n" + f"The probability of this diagnosis outcome is {diabetesProbability[0][0]}"

    else:

        return "Patient diagnosis is not diabetic. \n" + f"The probability of this diagnosis outcome is {diabetesProbability[0][0]}"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
