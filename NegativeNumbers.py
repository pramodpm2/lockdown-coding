'''
Given start and end of a range, write a Python program to print all negative numbers in given range.  
Example: Input: start = -4, end = 5 Output: -4, -3, -2, -1 Input: start = -3, end = 4 Output: -3, -2, -1
'''

start=int(input('Enter The Starting Number: '))
end=int(input('Enter The End Number: '))
print('\n')
print('All The Negtive Numbers In Range',start ,'To',end,'Is : ')
for i in range(start,end):
	if i<0:
		print(i ,end=' ')
print('\n')
