import streamlit as st
import pickle
import numpy as np


model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
#user_input1 = st.text_input("Input Year")
user_input1 = st.number_input("Input Year")
Year = 2020 - user_input1
#st.write(user_input1)
Present_Price = st.number_input("What is the Showroom Price?")
user_input3 = st.number_input("How many kilometers driven?")
Kms_Driven2 = np.log(user_input3)
Owner = st.number_input("Number of previous owners:")
user_input5 = st.selectbox('Fuel Type:', ['Petrol', 'Deisel','CNG'])
if user_input5 == 'Petrol':
    Fuel_Type_Petrol=1
    Fuel_Type_Diesel=0
elif user_input5 == 'Deisel':
    Fuel_Type_Petrol=0
    Fuel_Type_Diesel=1
else:
    Fuel_Type_Petrol=0
    Fuel_Type_Diesel=0
user_input6 = st.selectbox('Are you a dealer or an individual?', ['Individual', 'Dealer'])
if user_input6 == 'Individual':
    Seller_Type_Individual = 1
else:
    Seller_Type_Individual = 0

user_input7 = st.selectbox('Select transmission type', ['Manual', 'Automatic'])
if user_input7 == 'Manual':
    Transmission_Mannual = 1
else:
    Transmission_Mannual = 0
prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
output=round(prediction[0],2)
if output<0:
    st.write("Sorry you cannot sell this car")
else:
    st.write(f"You Can Sell The Car at {output}")
