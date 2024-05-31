import csv 
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt


Data = []

with open ('20_cycle.txt') as f:
    reader_obj = csv.reader(f) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    for row in reader_obj:

    # Load data into DataFrame
        Data.append(row)
# Data.remove([0])
# print(Data[0])
# res = list(filter(None, Data))
        
# print(Data[:1000])
# fcsv = []
# for data in Data:
#     t = data[0].split(',')
#     fcsv.append(t)
def dpa_to_bar(dpa):
    """
    Convert pressure from decipascal (dPa) to bar.

    Parameters:
    dpa (float): Pressure in decipascal.

    Returns:
    float: Pressure in bar.
    """
    # Conversion factor from dPa to bar
    conversion_factor = 1e-2
    
    # Convert dPa to bar
    bar = dpa * conversion_factor
    
    return bar
csd = []
for l in Data:
    if len(l) == 6:
        # csd.append([l[2],l[3],l[5]])
        if l[2] == "PRF" or l[2] == "FGN" or l[2] == "SDP" or l[2] == "DPD":
            csd.append([l[2],float(l[3].split()[1]),float(l[5].split()[1])])



        

# for d in range(10):
#     print(csd[d])

Prf = []
Flg = []
Stb = []
Dpd = []

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


for d in csd:
    if d[0] == "PRF":
        Prf.append([d[1],d[2]])
    elif d[0] == "FGN":
        Flg.append([d[1],d[2]])
    elif d[0] == "SDP":
        Stb.append([d[1],d[2]])


last = Stb[-1][1]
# print(last)
# print()

for d in csd:
    if d[0] == 'DPD':
        # print(d[2])
        p = last-dpa_to_bar(d[2])
        Dpd.append([d[1],p])
Final = Prf+Flg+Stb+Dpd
# # print(Prf)
# # print(Flg)
# print(Stb)
# print(Dpd)

columns = ['Elapse_Time', 'Pressure']
Pdf = pd.DataFrame(Final, columns=columns)
# Fdf = pd.DataFrame(Flg, columns=columns)
# Sdf = pd.DataFrame(Stb, columns=columns)
# Ddf = pd.DataFrame(Stb, columns=columns)

# # print(Pdf)
# # print(Fdf)
# # print(Sdf)
# # print(Ddf)

def dpa_to_bar1(dpa):
    """
    Convert pressure from decipascal (dPa) to bar.

    Parameters:
    dpa (float): Pressure in decipascal.

    Returns:
    float: Pressure in bar.
    """
    # Conversion factor from dPa to bar
    conversion_factor = 1e-4
    
    # Convert dPa to bar
    bar = dpa * conversion_factor
    
    return bar
Data1 = []

with open ('seal_Rejected.txt') as f:
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



        

# for d in range(10):
#     print(csd[d])

Prf1 = []
Flg1 = []
Stb1 = []
Dpd1 = []

empty1 = []

i = 0
for d in csd1:
    if d == ['PRF', 0.0, 0.0]:
        empty1.append(i)
    i += 1
f = empty1[0]
sec = empty1[1]

csd1 = csd1[f:sec]
# print(csd)


for d in csd1:
    if d[0] == "PRF":
        Prf1.append([d[1],d[2]])
    elif d[0] == "FGN":
        Flg1.append([d[1],d[2]])
    elif d[0] == "SDP":
        Stb1.append([d[1],d[2]])


last1 = Stb1[-1][1]
# print(last)
# print()

for d in csd1:
    if d[0] == 'DPD':
        # print(d[2])
        p = last-dpa_to_bar1(d[2])
        Dpd1.append([d[1],p])
Final1 = Prf1+Flg1+Stb1+Dpd1
# print(Final1)

defect = pd.DataFrame(Final1, columns=columns)




# # M_prf = Pdf['Pressure'].mean()
# # SD_prf = Pdf['Pressure'].std()

# # M_frf = Fdf['Pressure'].mean()
# # SD_frf = Fdf['Pressure'].std()

# # M_sdf = Sdf['Pressure'].mean()
# # SD_sdf = Sdf['Pressure'].std()

# # M_ddf = Ddf['Pressure'].mean()
# # SD_ddf = Ddf['Pressure'].std()

# # print(M_prf,SD_prf, '\n',M_frf,SD_frf,'\n',M_sdf,SD_sdf, '\n', M_ddf,  SD_ddf)

# ##   Plot

def dpa_to_bar2(dpa):
    """
    Convert pressure from decipascal (dPa) to bar.

    Parameters:
    dpa (float): Pressure in decipascal.

    Returns:
    float: Pressure in bar.
    """
    # Conversion factor from dPa to bar
    conversion_factor = 1e-4
    
    # Convert dPa to bar
    bar = dpa * conversion_factor
    
    return bar
Data2 = []

with open ('def3.txt') as f:
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



        

# for d in range(10):
#     print(csd[d])

Prf2 = []
Flg2 = []
Stb2 = []
Dpd2 = []

empty2 = []

i = 0
for d in csd2:
    if d == ['PRF', 0.0, 0.0]:
        empty2.append(i)
    i += 1
f = empty2[0]
sec = empty2[1]

csd2 = csd2[f:sec]
# print(csd)


for d in csd2:
    if d[0] == "PRF":
        Prf2.append([d[1],d[2]])
    elif d[0] == "FGN":
        Flg2.append([d[1],d[2]])
    elif d[0] == "SDP":
        Stb2.append([d[1],d[2]])


last2 = Stb2[-1][1]
# print(last)
# print()

for d in csd2:
    if d[0] == 'DPD':
        # print(d[2])
        p = last-dpa_to_bar2(d[2])
        Dpd2.append([d[1],p])
Final2 = Prf2+Flg2+Stb2+Dpd2
# print(Final1)

defect2 = pd.DataFrame(Final2, columns=columns)

plt.plot(Pdf['Elapse_Time'], Pdf['Pressure'],
             label=f'Okay', color='green', linewidth=0.3)
plt.plot(defect['Elapse_Time'], defect['Pressure'],
             label=f'Defect type 1', color='blue', linewidth=0.3)
plt.plot(defect2['Elapse_Time'], defect2['Pressure'],
             label=f'defect Type 2', color='red', linewidth=0.3)
# plt.plot(Ddf['Elapse_Time'], Ddf['Pressure'],
#              label=f'Graph extra Stablizing', color='black', linewidth=0.5)
# # Add labels and title
plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Multiple Graphs')

# Add legend
plt.legend()

# Show the plot
plt.show()




# # Separate the data into cycles
# cycles = []
# current_cycle = []

# for row in csd:
#     if row == ['PRF', 0.0, 0.0] and current_cycle:
#         cycles.append(current_cycle)
#         current_cycle = [row]
#     else:
#         current_cycle.append(row)
# cycles.append(current_cycle)  # Append the last cycle

# # Plotting
# plt.figure(figsize=(10, 6))

# for cycle in cycles:
#     times = [row[1] for row in cycle]
#     values = [row[2] for row in cycle]
#     plt.plot(times, values, marker='o', label=f'Cycle {cycles.index(cycle) + 1}')

# plt.xlabel('Time')
# plt.ylabel('Value')
# plt.title('Cycle Data')
# plt.legend()
# plt.grid(True)
# plt.show()

