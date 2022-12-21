import streamlit as st
import requests
import pandas as pd
import numpy as np

'# ML Case Study - Logistic Regression on 2 parameters '

'### What are the features values ?'
sum_paid_inv_0_12m = st.number_input('sum_paid_inv_0_12m', 0)
time_hours = st.number_input('time_hours', 0.0)

API_url = 'https://mlcasestudy-ybspnrtpla-ew.a.run.app/predict'

X_dict = {'sum_paid_inv_0_12m':sum_paid_inv_0_12m,
          'time_hours':time_hours}

#Getting and saving request's response
response = requests.get(url=API_url, params=X_dict).json()

#Displaying response
f"The predicted default status is {response['default']}"
f"Probability to get a 0-default is : {round(response['y_pred_proba_zero'],2)}."
f"Probability to get a 1-default is : {round(response['y_pred_proba_one'],2)}."
