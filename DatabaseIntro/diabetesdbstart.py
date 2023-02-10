from pathlib import Path
import pandas as pd
import sqlite3

Path('DNFinal_Project.db').touch()
conn = sqlite3.connect('DNFinal_Project.db')
c = conn.cursor()
c.execute('''CREATE TABLE diabetesraw (Pregnancies int, Glucose int, BloodPressure int, SkinThickness int, Insulin int, BMI int, DiabetesPedigreeFunction int, Age int, Outcome int)''')
# load the data into a Pandas DataFrame
diabetesraw = pd.read_csv('diabetesraw.csv')
# write the data to a sqlite table
diabetesraw.to_sql('diabetesraw', conn, if_exists='append', index=False)
c.execute('''SELECT * FROM diabetesraw''').fetchall()
conn.commit()
# closing the database connection
conn.close()


# engine = create_engine("sqlite:///DNFinal_project.sqlite")
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# Glucose = Base.classes.glucose

# session = Session(engine)
# results = session.query(Glucose.glucose).all()
# Glucose = list(np.ravel(results))
# return jsonify(Glucose=Glucose)

# # conn = sqlite3.connect('DNFinal_Project.db')
# c = conn.cursor()

# c.execute('''SELECT * FROM diabetes''').fetchall()
# conn.commit()
# closing the database connection
# conn.close()
