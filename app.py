import numpy as np 
import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression
import tensorflow as tf
from tensorflow.keras import Sequential
import keras
from keras.models import load_model
import pickle
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)
# model = pickle.load(open("trained_model_dnn.sav", "rb"))
model_f = keras.models.load_model('trained_model.h5')
rb_scaler = joblib.load("RobustScaler")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	step = request.form["TransactionHour"]
	type = request.form["TransactionType"]
	amount = request.form["TransactionAmount"]
	# nameOrig = request.form["Origin_Name"]
	oldbalanceOrig = request.form["Old_Balance_Origin"]
	newbalanceOrig = request.form["New_Balance_Origin"]
	# nameDest = request.form["Destination_Name"]
	oldbalanceDest = request.form["Old_Balance_Destination"]
	newbalanceDest = request.form["New_Balance_Destination"]
	isFlaggedFraud = request.form["FraudFlag"]
	
	# Balance Differences: Origin & Destination
	diffOrig = int(oldbalanceOrig) - int(newbalanceOrig)
	diffDest = int(oldbalanceDest) - int(newbalanceDest)

	# Data Preparation: Encoding & Normalization
	if (type=='CASH_IN'):
		encoded_type = 0
	elif (type=='CASH_OUT'):
		encoded_type = 1
	elif (type=='DEBIT'):
		encoded_type = 2
	elif (type=='PAYMENT'):
		encoded_type = 3
	else:
		encoded_type = 4

	# Create a Query DataFrame
	query_df = pd.DataFrame([[step,encoded_type,amount,isFlaggedFraud,diffOrig,diffDest]],columns=['step','encoded_type','amount','isFlaggedFraud','diffOrig','diffDest'])

	
	query_df = rb_scaler.transform(query_df)
	
	prediction=model_f.predict(query_df)

	if prediction == 1:
		return render_template('home.html',prediction_text="Red Flag")
	else:
		return render_template('home.html',prediction_text="Green Flag")


if __name__ == "__main__":
    app.run(debug=True)
