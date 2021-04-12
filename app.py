from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('xb_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Carat = float(request.form['Carat'])
        Cut=int(request.form['Cut'])
        Color=int(request.form['Color'])
        Clarity=int(request.form['Clarity'])
        Depth=float(request.form['Depth'])
        Table=float(request.form['Table'])
        x=float(request.form['x'])
        y=float(request.form['y'])
        z=float(request.form['z'])

        prediction=model.predict(pd.DataFrame({'carat':[Carat], 'cut':[Cut], 'color':[Color],
                      'clarity':[Clarity], 'depth':[Depth],
                      'table':[Table], 'x':[x],
                      'y':[y], 'z':[z]}))

        if prediction<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="Price {}".format(prediction))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
