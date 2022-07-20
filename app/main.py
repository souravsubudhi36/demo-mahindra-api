# from unittest import result
# import pandas as pd
from flask import Flask, json, render_template
from flask.globals import request
from flask import Flask, jsonify
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

model = pickle.load(open('app/aeration_rpm.pickle' , 'rb'))
 
@app.route("/")
def home_view():
        return "<h1>Welcome to Geeks for Geeks</h1>"

@app.route("/aeration_rpm" , methods = ['POST'])
def rpm_calculator():
    try:
        
        _json = request.json
        BOD_value = _json['sensor_value']
        print(BOD_value)
        BOD_value = int(BOD_value)
        input_BOD = np.array([BOD_value])
        input_BOD = input_BOD.reshape(1 , -1)
        temp = model.predict(input_BOD)
        result = temp[0][0]
        print(result)
        result = jsonify(result)
        result.status_code = 200
        return result
    except Exception as e:
        print(e)
        

# if __name__ == '__main__':
#     app.run(port = 5000, debug=True)