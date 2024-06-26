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

Data = []

with open ('Part_Accepted.txt') as f:
    reader_obj = csv.reader(f) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    for row in reader_obj:

    # Load data into DataFrame
        Data.append(row)

csd = []
for l in Data:
    if len(l) == 6:
        # csd.append([l[2],l[3],l[5]])
        if l[2] == "PRF" or l[2] == "FGN" or l[2] == "SDP":
            csd.append([l[2],float(l[3].split()[1]),float(l[5].split()[1])])


            


empty = []

i = 0
for d in csd:
    if d == ['PRF', 0.0, 0.0]:
        empty.append(i)
    i += 1
f = empty[0]
sec = empty[1]

csd = csd[f:sec]

# print(csd)
D = []
den = []
for d in csd:
    D.append([d[1],d[2]])
    den.append(d[2])


columns = ['Elapse_Time', 'Pressure']
data = pd.DataFrame(D, columns=columns)
# print(data)



###                 MAJOR                   #########

Data1 = []

with open ('Part_Rejected.txt') as f:
    reader_obj = csv.reader(f) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    for row in reader_obj:

    # Load data into DataFrame
        Data1.append(row)

csd1 = []
for l in Data1:
    if len(l) == 6:
        # csd.append([l[2],l[3],l[5]])
        if l[2] == "PRF" or l[2] == "FGN" or l[2] == "SDP" or l[2] == "DPD":
            csd1.append([l[2],float(l[3].split()[1]),float(l[5].split()[1])])

empty = []

i = 0
for d in csd1:
    if d == ['PRF', 0.0, 0.0]:
        empty.append(i)
    i += 1
f = empty[0]
sec = empty[1]

csd1 = csd1[f:sec]

# print(csd)
D1 = []
den = []
for d in csd:
    D1.append([d[1],d[2]])

columns = ['Elapse_Time', 'Pressure']
datamajor = pd.DataFrame(D1, columns=columns)


###                 Minor                   #########

Data2 = []

with open ('stab.txt') as f:
    reader_obj = csv.reader(f) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    for row in reader_obj:

    # Load data into DataFrame
        Data2.append(row)

csd2 = []
for l in Data2:
    if len(l) == 6:
        # csd.append([l[2],l[3],l[5]])
        if l[2] == "PRF" or l[2] == "FGN" or l[2] == "SDP" or l[2] == "DPD":
            csd2.append([l[2],float(l[3].split()[1]),float(l[5].split()[1])])

empty = []

i = 0
for d in csd2:
    if d == ['PRF', 0.0, 0.0]:
        empty.append(i)
    i += 1
f = empty[0]
sec = empty[1]

csd2 = csd2[f:sec]

# print(csd)
D2 = []
den = []
for d in csd:
    D2.append([d[1],d[2]])

columns = ['Elapse_Time', 'Pressure1']
dataminor = pd.DataFrame(D2, columns=columns)






df1 = datamajor.rename(columns={'Pressure': 'Pressure for Rejected'})
df2 = dataminor.rename(columns={'Pressure1': 'Stab'})

# Merge DataFrames on 'x' column
df_combined = pd.merge(df1, df2, on='Elapse_Time')

# Set 'x' column as the index
df_combined = df_combined.set_index('Elapse_Time')


with c2:
    tab1, tab2 = st.tabs(["Chart", "Table"])

    with tab1:


    # Create columns
        col1, col2 = st.columns(2)

        with col1:

            st.line_chart(data=data, x='Elapse_Time', y='Pressure', color='#00FF00', width=0, height=0, use_container_width=True)
        with col2:
            st.line_chart(data=datamajor, x='Elapse_Time', y='Pressure', color='#FF0000', width=0, height=0, use_container_width=True)

        st.line_chart(data=df_combined, color=['#FF0000','#001fff'] ,width=0, height=0, use_container_width=True)

    with tab2:
        Col1, Col2 = st.columns(2)
        with Col1:

            st.header("Data table for Part Accepted")
            
            st.dataframe(data)
        with Col2:

            st.header("Data table for Part Rejected")   
            
            st.dataframe(datamajor)