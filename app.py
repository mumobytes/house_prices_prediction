import streamlit as st 
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learning to predict house prices with given feature of the house."
         "For using this app you can enter the inputs from this UI and then use predict button.")

st.divider()

bedrooms = st.number_input("Number of bedrooms ", min_value = 0, value = 0)
bathrooms = st.number_input("Number of bathrooms", min_value = 0, value = 0)
living_area = st.number_input("Living Area ", min_value = 0 , value = 2000)
condition = st.number_input("Condition", min_value =0, value= 3)
NumberofSchools = st.number_input("Number of schools nearby ", min_value= 0 , value= 0)

st.divider()

X =[[bedrooms,bathrooms,living_area,condition,NumberofSchools]]

predictbutton = st.button("Predict!")

if predictbutton:
    
    st.balloons()
    
    X_array = np.array(X)
    
    prediction = model.predict(X_array)
    
    st.write(f"Predicted Price: KSh {prediction[0]:,.0f}")
else: 
    st.write("Please use predict button after entering values")



#Order of X ['number of bedrooms', 'number of bathrooms', 'living area',
       #'condition of the house', 'Number of schools nearby']