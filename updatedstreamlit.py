import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load the trained model
with open('trained_model1.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the scaler used during training
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Define a function to preprocess user input
def preprocess_input(et_time, t_time, pressure):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'ET_Time': [et_time],
        'T_Time': [t_time],
        'Pressure': [pressure]
    })
    
    # Scale the input data using the same scaler used during training
    input_data_scaled = scaler.transform(input_data)
    return input_data_scaled

# Streamlit app
st.title('CTS Leak Test Model Deployment')

st.write("""
# Welcome to the CTS Leak Test Prediction App!
This app uses a Random Forest Classifier to predict if the given test parameters are accepted or rejected.
""")

# Example values for users to understand the accepted/rejected criteria
st.write("""
## Accepted Values Example:
- Pressure: `3.0` bar (greater than 2.5 bar)
- ET Time: `17.0` sec (less than or equal to 18 sec)
- T Time: `14.0` sec (less than or equal to 15 sec)

## Rejected Values Example:
- Pressure: `2.4` bar (less than 2.5 bar)
- ET Time: `19.0` sec (greater than 18 sec)
- T Time: `16.0` sec (greater than 15 sec)
""")

# Input fields
et_time = st.number_input('Enter ET Time (sec)', min_value=0.0, max_value=30.0, value=17.0, step=0.1)
t_time = st.number_input('Enter T Time (sec)', min_value=0.0, max_value=30.0, value=14.0, step=0.1)
pressure = st.number_input('Enter Pressure (bar)', min_value=0.0, max_value=10.0, value=3.0, step=0.1)

# Debugging prints to check input values
st.write(f'Input ET Time: {et_time}')
st.write(f'Input T Time: {t_time}')
st.write(f'Input Pressure: {pressure}')

# Predict button
if st.button('Predict'):
    input_data = preprocess_input(et_time, t_time, pressure)
    
    # Debugging prints to check preprocessed values
    st.write(f'Preprocessed Input: {input_data}')
    
    prediction = model.predict(input_data)[0]
    
    # Show the result
    if prediction == 1:
        st.success('Accepted')
    else:
        st.error('Rejected')
