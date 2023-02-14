import sqlite3, csv

connection = sqlite3.connect("diabetes.db")
cursor = connection.cursor()

with open("diabetes.csv", "r") as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO diabetesTable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print("\n{} Records Transfered".format(no_records))
