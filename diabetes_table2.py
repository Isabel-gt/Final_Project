
from pathlib import Path
import pandas as pd
import sqlite3
import csv


Path('diabetes.db').touch()
connection = sqlite3.connect("diabetes.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE diabetesTable3 ('Diabetes_binary', 'HighBP', 'CholCheck', 'Smoker', 'Stroke', 'PhysActivity', 'NoDocbcCost', 'Sex', 'BMI', 'Age', 'Education')''')
with open("diabetes2.csv", "r") as file:
    no_records = 0
    for row in file:
        cursor.execute(
            "INSERT INTO diabetesTable3 VALUES (?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print("\n{} Records Transfered".format(no_records))
