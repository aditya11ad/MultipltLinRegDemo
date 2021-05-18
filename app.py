from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('lr.pkl', 'rb'))
@app.route('/')

def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Rd = int(request.form['rd'])
        Adm=float(request.form['adm'])
        Mrkt=int(request.form['mrkt'])
        State=request.form['state']
        if(State=='New York'):
            St_Florida=0
            St_NY=1
        elif(State=='California'):
            St_Florida=0
            St_NY=0
        else:
            St_Florida=1
            St_NY=0
        prediction=model.predict([[Rd,Adm,Mrkt,St_Florida,St_NY]])
        output=round(prediction[0],2)
        
        return render_template('index.html',prediction_text="Predicted Profit is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)

