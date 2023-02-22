from flask import Flask,request, render_template
import numpy as np
import tensorflow as tf

app = Flask(__name__)

model =tf.keras.models.load_model('my_model')


@app.route('/')
def hello_world():
    return render_template("inputs.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    final = np.reshape(final, (1, -1))
    
    print(int_features)
    print(final)
    prediction=model.predict(final)
    # output = prediction[0]
    output=prediction[0]

    if output > 0.5:
        return render_template('inputs.html',pred='Your health is in Danger.\nProbability of Diabetes is {}%'.format(output*100))
    else:
        return render_template('inputs.html',pred='You are NOT likely to have Diabetes.\n Probability of Diabetes is {}%'.format(output*100))


if __name__ == '__main__':
    app.run(debug=True)