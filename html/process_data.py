from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# load the model
model = tf.keras.models.load_model('my_model')

# define a route for the predict function
@app.route('/', methods=['POST'])
def process_data():
    input1 = request.form['input1']
    input2 = request.form['input2']
    input3 = request.form['input3']
    input4 = request.form['input4']
    input5 = request.form['input5']
    input6 = request.form['input6']
    input7 = request.form['input7']
    input8 = request.form['input8']
    input9 = request.form['input9']
    input10 = request.form['input10']
    

    
    result1 = model.predict(input_data)
    
   
    return render_template('output.html', result1=result1)


input_data = process_data()

if __name__ == '__main__':
    app.run()