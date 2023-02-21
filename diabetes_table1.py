import sqlite3, csv

connection = sqlite3.connect("diabetes3.db")
cursor = connection.cursor()

with open("diabetes3.csv", "r") as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO diabetesTable3 VALUES (?,?,?,?,?,?,?,?,?,?,?)", row.split(","))
        connection.commit()
        no_records += 1
connection.close()
print("\n{} Records Transfered".format(no_records))
