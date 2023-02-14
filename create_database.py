import sqlite3
conn = sqlite3.connect("diabetes.db")
cur = conn.cursor()

sql = """
    CREATE TABLE diabetesTable (
        Diabetes_012 INTEGER,
        HighBP INTEGER, 
        HighChol INTEGER,
        CholCheck INTEGER,
        BMI INTEGER,
        Smoker INTEGER,
        Stroke INTEGER,
        HeartDiseaseorAttack INTEGER,
        PhysActivity INTEGER,
        Fruits INTEGER,
        Veggies INTEGER,
        HvyAlcoholConsump INTEGER,
        AnyHealthcare INTEGER,
        NoDocbcCost INTEGER,
        GenHlth INTEGER,
        MentHlth INTEGER,
        PhysHlth INTEGER,
        DiffWalk INTEGER,
        Sex INTEGER,
        Age INTEGER,
        Education INTEGER,
        Income INTEGER
    ) """

cur.execute(sql)
print("diabetesTable has been created.")

conn.commit()
conn.close()