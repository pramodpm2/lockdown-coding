import numpy as np 
R = int(input("Enter the number of rows:")) 

C = int(input("Enter the number of columns:")
) 
print("Enter the entries in a single line (separated by space): ") 

entries = list(map(int, input().split())) 

matrix = np.array(entries).reshape(R, C) 
print('Matrix Before Rotation: ')
print(matrix) 
rmat=np.rot90(matrix)
print('Matrix After Rotation Of 90 Degree: ')
print(rmat)
