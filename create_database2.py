import sqlite3
conn = sqlite3.connect("diabetes3.db")
cur = conn.cursor()

sql = """
    CREATE TABLE diabetesTable3 (
        Diabetes INTEGER,
        HighBP INTEGER, 
        CholCheck INTEGER,
        Smoker INTEGER,
        Stoke INTEGER,
        PhysActivity INTEGER,
        NoDocbcCost INTEGER,
        Sex INTEGER,
        BMI INTEGER,
        Age INTEGER,
        Education INTEGER
    ) """

cur.execute(sql)
print("diabetesTable has been created.")

conn.commit()
conn.close()