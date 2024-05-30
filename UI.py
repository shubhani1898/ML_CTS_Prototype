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

#####                   Different Dataset           #########

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
import random
TIME_FACTOR = 1 + random.random()
PRESSURE_FACTOR = 1 + random.random()
D1 = []
den = []
for d in csd:
    D1.append([d[1],d[2]])

columns = ['Elapse_Time', 'Pressure']
datamajor = pd.DataFrame(D1, columns=columns)
datamajor['Pressure'] = datamajor['Pressure'] * 1.2


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



# Sample Data
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
pressure_cal_cycle_1 = [0, 2, 3.8, 4.7, 4.9, 4.98, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0]  # No leak
defect1 = [0, 2, 3.8, 4.7, 4.9, 4.98, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4.9, 4.8, 4.8, 0]  #  leak
defect2 = [0, 2, 3.8, 4.7, 4.9, 4.98, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4.9, 4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 0]  # Corrected leak
defect3 = [0, 2, 3.8, 4.7, 4.9, 4.98, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4.9, 4.8, 4.7, 4.7, 4.5, 4.3, 4.3, 0]  # No leak

# Time =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# Pressure_Cycle1 = [0, 2, 3.8, 4.7, 4.9, 4.98, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0]
# Pressure_Cycle4 = [4.9689, 5.0645, 5.0643, 4.9035, 4.9322, 4.9904, 5.0599, 5.0421, 5.0671, 5.0640, 5.0373, 5.0427, 4.9124, 4.9513, 5.0331, 5.0483, 4.9617, 4.9948, 4.9753, 5.0358, 4.9622, 4.9052, 4.9030, 4.9660, 4.9769, 4.9163]
# Pressure_Cycle5 = [0.0000, 2.0000, 2.1249, 2.2746, 2.4706, 2.6511, 2.7689, 2.8800, 3.0790, 3.2439, 3.3606, 3.4936, 3.6891, 3.8182, 3.9283, 3.7471, 3.6083, 3.4586, 3.2761, 3.1565, 3.0314, 2.9147, 2.7688, 2.6670, 2.5269, 2.4057]
# Pressure_Cycle6 = [0.0000, 2.1581, 2.3055, 2.4125, 2.5312, 2.6616, 2.7967, 3.1264, 4.2583, 5.7033, 6.8056, 8.1205, 9.3093, 9.1382, 8.9770, 8.7802, 8.6228, 8.4806, 8.3231, 8.1381, 8.0186, 7.8488, 7.7383, 7.5926,0.0000]
# Create a DataFrame
randomdata = {
    'Time': time,
    'Pressure Cycle 1': pressure_cal_cycle_1,
    
}
randomdata1 = {
    'Time': time,
    'Pressure Cycle 1': pressure_cal_cycle_1,
    'decect': defect2
}
randomdata2 = {
    'Time': time,
    'defect1': defect1,
    'defect2': defect2,
    'defect3': defect3
}

df = pd.DataFrame(randomdata)
df1 = pd.DataFrame(randomdata1)
df2 = pd.DataFrame(randomdata2)


# NewSample = {
#     'Time': Time,
#     'Pressure_Cycle1': Pressure_Cycle1,
#     'Pressure_Cycle4': Pressure_Cycle4,
#     'Pressure_Cycle5': Pressure_Cycle5,
#     'Pressure_Cycle6':Pressure_Cycle6

# }
# Newdf = pd.DataFrame(NewSample)




with col1:
    st.header("""
            Dataset
          """)
    st.dataframe(df)
    st.dataframe(df1)

with col2:
    st.header('Pressure Calibration Cycles')

    # Plot the data using st.line_chart
    st.line_chart(df2.set_index('Time'), color=['#FF0000','#001fff','#00FF00'])
    # st.line_chart(Newdf.set_index('Time'))

    c1,c2 = st.columns([1,1])
    with c1:
            st.header('No Pressure detect')
            st.line_chart(df.set_index('Time'))
            # st.line_chart(df1.set_index('Time'), color=['#FF0000','#001fff'])
    # st.line_chart(data=datamajor, x='Elapse_Time', y='Pressure', color='#11FF11', width=0, height=0, use_container_width=True)
    with c2:
    #     st.title('Pressure for multiple cycle')
    #     st.line_chart(data=df_combined, color=['#FF0000','#001fff'] ,width=0, height=0, use_container_width=True)
    # # Streamlit application
        st.header('Leak vs Okay')
        st.line_chart(df1.set_index('Time'), color=['#FF0000','#001fff'])
        
    
    