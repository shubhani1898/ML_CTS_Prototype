import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
import csv
from streamlit_extras.app_logo import add_logo

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



st.image('TASI.png',width=150)
# st.add_logo('TASI.png')

c1,c2 = st.columns([1,2],gap='large')

with c1:

# Streamlit app
    # st.title('CTS Leak Test Model Deployment')

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



# with c2:
#     tab1, tab2 = st.tabs(["Chart", "Table"])

#     with tab1:


#     # Create columns
#         col1, col2 = st.columns(2)

#         with col1:

#             st.line_chart(data=data, x='Elapse_Time', y='Pressure', color='#00FF00', width=0, height=0, use_container_width=True)
#         with col2:
#             st.line_chart(data=datamajor, x='Elapse_Time', y='Pressure', color='#FF0000', width=0, height=0, use_container_width=True)

#         st.line_chart(data=df_combined, color=['#FF0000','#001fff'] ,width=0, height=0, use_container_width=True)

#     with tab2:
#         Col1, Col2 = st.columns(2)
#         with Col1:

#             st.header("Data table for Part Accepted")
            
#             st.dataframe(data)
#         with Col2:

#             st.header("Data table for Part Rejected")   
            
#             st.dataframe(datamajor)