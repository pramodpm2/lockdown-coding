'''

Write Python Program to Reverse a Given Number
This is a Python Program to reverse a given number.
Problem Description
The program takes a number and reverses it and store it in another variable and show it
'''



n=int(input('Enter The Number: '))
rev=0
a=0
while n>0:
	a=n%10
	rev=rev*10+a
	n=n//10
print('Thr Revers Number Is: ',rev)
	
