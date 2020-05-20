x=int(input('Enter x: '))
y=int(input('Enter y: '))

print('Before Swaping: x = ',x,'y = ',y)
x = x ^ y;
y = x ^ y;
x = x ^ y;
print ("After Swapping: x = ", x,"y = ", y)
