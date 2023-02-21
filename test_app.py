from flask import Flask,request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model2.pkl','rb'))

def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    final = np.reshape(final, (1, -1))
    
    print(int_features)
    print(final)
    prediction=model.predict(final)
    
    print(prediction)