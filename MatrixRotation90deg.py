'''
Matrix Rotation by 90 Degree in Clockwise Direction:

Input:
Enter the total Number of Rows m: 3
Enter the total Number of Columns: 3
Enter the Elements of the Matrix:
1 2 3 4 5 6 7 8 9
Output:
The Given Matrix is:
1 2 3
4 5 6
7 8 9
The Output Matrix After Rotation by 90 Degree in Clockwise Direction is:
7 4 1
8 5 2
9 6 3

Matrix Rotation by 90 Degree in Anticlockwise Direction:

Input:
Enter the total Number of Rows m: 3
Enter the total Number of Columns: 3
Enter the Elements of the Matrix:
1 2 3 4 5 6 7 8 9
Output:
The Given Matrix is:
1 2 3
4 5 6
7 8 9

The Output Matrix After Rotation by 90 Degree in Clockwise Direction is:
3 6 9
2 5 8
1 4 7
'''



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
