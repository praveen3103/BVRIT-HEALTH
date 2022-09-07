from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Bvrit_health_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Age = int(request.form['Age'])
        Vata=int(request.form['Present vata'])
        Pitta=int(request.form['Present pitta'])
        Kapha=int(request.form['Present kapha'])
        Gender_M=request.form['Gender']
        if(Gender_M=='male'):
            Gender_M=1
            Gender_F=0
        
        else:
            Gender_M=0
            Gender_F=1
        prediction=model.predict([[Vata,Pitta,Kapha,Age,Gender_M,Gender_F]])
        output=round(prediction[0],1)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry we cant predict your health")
        else:
            return render_template('index.html',prediction_text="Your vata is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)