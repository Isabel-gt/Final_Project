from pathlib import Path
import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return ("<h1>Hello Everyone!</h1>")


@app.route("/homepage")
def homepage():
    return render_template("test.html")


@ app.route("/intro")
def intro():
    # engine = create_engine("sqlite:///DNFinal_project.sqlite")
    # Base = automap_base()
    # Base.prepare(engine, reflect=True)
    # Glucose = Base.classes.glucose

    # session = Session(engine)
    # results = session.query(Glucose.glucose).all()
    # Glucose = list(np.ravel(results))
    # return jsonify(Glucose=Glucose)
    return ("<h1>Introduction Dataset and Model Selection</h1>"
            '''
            route to dataset:
            /api/v1.0/diabetesraw

            ''')

# conn = sqlite3.connect('DNFinal_Project.db')
# c = conn.cursor()

# c.execute('''SELECT * FROM diabetes''').fetchall()
# conn.commit()
# closing the database connection
# conn.close()


@ app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template(model.html)


@ app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


@ app.route("/viz")
def viz():
    return "<h1>Data Visualization and Insights</h1>"


@ app.route("/model")
def model():
    return "<h1>Model Training And Testing</h1>"


# @ app.route("/<name>")
# defuser(name):
#    return f"<h2>Hello {name}! Please fill out the questionnaire below</h2>"


@ app.route("/eval")
def eval():
    return "<h1>Accuracy Scores Comparison And Model Selection</h1>"


@ app.route("/end")
def end():
    return "<h1>Summary Conclusion And Recommendation</h1>"


@ app.route("/admin")
def admin():
    return(url_for("/"))


if __name__ == "__main__":
    app.run()
