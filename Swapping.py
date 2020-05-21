'''
Write Python Program to Reverse a Given Number
This is a Python Program to reverse a given number.
Problem Description
The program takes a number and reverses it and store it in another variable and show it
'''



x=int(input('Enter x: '))
y=int(input('Enter y: '))

print('Before Swaping: x = ',x,'y = ',y)
x = x ^ y;
y = x ^ y;
x = x ^ y;
print ("After Swapping: x = ", x,"y = ", y)
