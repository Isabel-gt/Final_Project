from pathlib import Path
import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from DiabetesPrediction import BalancedRandomForestClassifier
from flask import Flask, jsonify, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@ app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template(test.html)


@ app.route("/database")
def database():
    return f"<h1> Main Table </h1>" f"<h2> Feature Table </h2>"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
