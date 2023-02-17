import sqlite3
conn = sqlite3.connect("diabetes3.db")
cur = conn.cursor()

sql = """
    CREATE TABLE diabetesTable3 (
        Education INTEGER,
        Age INTEGER, 
        HighBP INTEGER,
        Sex INTEGER,
        BMI INTEGER,
        CholCheck INTEGER,
        NoDocbcCost INTEGER,
        Stoke INTEGER,
        Smoker INTEGER,
        PhysActivity INTEGER,
        Diabetes_012 INTEGER
    ) """

cur.execute(sql)
print("diabetesTable has been created.")

conn.commit()
conn.close()