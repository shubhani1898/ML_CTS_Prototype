import csv

Data = []

with open ('new3.csv') as f:
    reader_obj = csv.reader(f) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    for row in reader_obj:

    # Load data into DataFrame
        Data.append(row)

# print(Data[0])
        
for i in range(10):
    print(Data[i])

PART = []
SEALED = []
LEAK = []
for d in Data[:1411]:
    
    if d[3] == 'Part1':
        PART.append([d[0],d[1],d[9]])
    elif d[3] == 'Part2':
        PART.append([d[0],d[1],d[9]])
    elif d[3] == 'Part3':
        PART.append([d[0],d[1],d[9]])

print(PART)
print(SEALED)
print(LEAK)
    
    