import streamlit as st
import numpy as np
import pandas as pd
import csv


l,banner = st.columns([1,1])

with l:

    st.image('TASI.png',width=200)
with banner:
    st.title("AI Predictive ")

col1,col2 = st.columns([1,2])

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

for d in csd:
    D.append([d[0],d[1],d[2]])
    


columns = ['Phase','Elapse_Time', 'Pressure']
data = pd.DataFrame(D, columns=columns)

#####                   Different Dataset               ###########
Data1 = []

with open ('new3.csv') as f:
    reader_obj = csv.reader(f) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    for row in reader_obj:

    # Load data into DataFrame
        Data1.append(row)

# print(Data[0])
        
for i in range(10):
    print(Data1[i])

PART = []

for d in Data1:
    
    if d[3] == 'Part3':
        PART.append([d[0],d[1],d[9]])

columns1 = ['Elapse_Time', 'Pressure','Label']
data1 = pd.DataFrame(D, columns=columns1)


with col1:
    st.header("""
            Dataset
          """)
    st.dataframe(data)

with col2:
    st.line_chart(data=data, x='Elapse_Time', y='Pressure', color='#00FF00', width=0, height=0, use_container_width=True)
    st.line_chart(data=data1, x='Elapse_Time', y='Pressure', color='#FF0000', width=0, height=0, use_container_width=True)
    
