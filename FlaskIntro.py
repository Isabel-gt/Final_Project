from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score
##from imblearn.ensemble import BalancedRandomForestClassifier
#from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
#import tensorflow as tf
import warnings
import math
from sklearn import metrics
import pickle
from flask import Flask, jsonify, redirect, url_for, render_template, request

app = Flask(__name__)


model = pickle.load(open('model.pkl', 'rb'))

#modelr = pickle.load(open('modelr.pkl', 'rb'))
#model1 = pickle.load(open('model1.pkl', 'rb'))
#model2 = pickle.load(open('model2.pkl', 'rb'))


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@ app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        return request.form.get('validate5')
    
        #num_values = [int(x) for x in request.form.getlist('validate')]
        #values = [np.array(num_values)]
        #prediction = model.predict_proba(features)
        #result = '{o.{1}f}'.format(prediction[0][1, 2])

        # if result > str(0.6):
        #     return render_template("index.html", pred='Additionnal Testing Advised.\n Probability of pre-diabetes is {}'.format(result))
        # else:
        #     return render_template("index.html", pred='Continue Usual Care.\n Probability of pre-diabetes is {}'.format(result))


@ app.route("/testr", methods=["POST", "GET"])
def testr():
    num_features = [int(x) for x in request.form.values()]
    features = [np.array(num_features)]
    prediction = modelr.predict_proba(features)
    result = '{o.{1}f}'.format(prediction[0][1, 2])

    if result > str(0.6):
        return render_template("index.html", pred='Additionnal Testing Advised.\n Probability of pre-diabetes is {}'.format(result))
    else:
        return render_template("index.html", pred='Continue Usual Care.\n Probability of pre-diabetes is {}'.format(result))


# @ app.route("/test2", methods=["POST", "GET"])
# def test2():
    num_features = [int(x) for x in request.form.values()]
    features = [np.array(num_features)]
    prediction = model2.predict_proba(features)
    result = '{o.{1}f}'.format(prediction[0][1, 2])

    if result > str(0.6):
        return render_template("index.html", pred='Additionnal Testing Advised.\n Probability of pre-diabetes is {}'.format(result))
    else:
        return render_template("index.html", pred='Continue Usual Care.\n Probability of pre-diabetes is {}'.format(result))


# @ app.route("/database")
# def database():
    # return f"<h1> Main Table </h1>" f"<h2> Feature Table </h2>"P


if __name__ == "__main__":
    app.run(port=5000, debug=True)
