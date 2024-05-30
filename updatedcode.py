# import csv

# Data1 = []

# with open ('new3.csv') as f:
#     reader_obj = csv.reader(f) 
      
#     # Iterate over each row in the csv  
#     # file using reader object 
#     for row in reader_obj:

#     # Load data into DataFrame
#         Data1.append(row)

# # print(Data1[100][0])
        
# # for i in range(10):
# #     print(Data1[i])
# # for d in Data1[0:10]:
# #     print(d[0],d[1],d[9])

# PART = []

# for d in Data1:
    
#     if d[3] == 'Part2':
#         PART.append([d[0],d[1],d[9]])
    

# print(len(PART))

    
    

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
data = pd.read_csv('new3.csv', header=None)
data.columns = ['Timestamp', 'Pressure', 'Phase', 'PartID', 'Val1', 'Val2', 'Val3', 'Val4', 'Val5', 'LeakType']

# Streamlit application
st.title('Line Chart for Each PartID')

# Get unique PartIDs
part_ids = data['PartID'].unique()

# Plot the data
plt.figure(figsize=(10, 6))
for part_id in part_ids:
    part_data = data[data['PartID'] == part_id]
    plt.plot(part_data['Timestamp'], part_data['Pressure'], label=f'PartID: {part_id}')

plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Pressure vs Time for Each PartID')
plt.legend()
plt.grid(True)

# Show the plot in Streamlit
st.pyplot(plt)
