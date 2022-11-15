import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


app=Flask(__name__)
#Load the model
model=pickle.load(open('regression.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html') #whenever we enter we have to go to the home page. This will look at a template folder.

@app.route('/predict_api',methods=['POST']) #send request to app and get output hence post
def predict_api():
    data=request.json['data'] # whenever predict_api is used give input in json format and that is stored in data variable
    print(data)
    print(np.array(list(data.values())).reshape(1,-1)) 
    item=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=model.predict(item) #whenever new data is passed to the model always reshape
   # output=model.predict()
    print(output[0]) # because output is 2D
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()] # giving float values because all our features are in float for this dataset
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=model.predict(final_input)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)


