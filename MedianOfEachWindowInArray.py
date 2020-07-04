'''

Examples: Input: arr[] = {-1, 5, 13, 8, 2, 3, 3, 1}, k = 3 Output: 5 8 8 3 3 3 Input: arr[] = {-1, 5, 13, 8, 2, 3, 3, 1}, k = 4 Output: 6.5 6.5 5.5 3.0 2.5
'''

n=int(input('Enter Number Of Elements: '))
k=int(input('Enter The K Value: '))
a=[]
print('Enter The All Elements In Single Line: ')
for i in range(0,n):
	a.append(int(input()))
b=[]
c=[]
rear=0
count=0
front=k
while(1):
	while(count<front):
		b.append(a[count])
		count+=1
	b.sort()
	front+=1
	rear+=1
	count=rear
	print(b)
	length=len(b)
	
	if length%2!=0:
		index=length//2
		c.append(b[index])
	else:
		index=length//2
		c.append((b[index]+b[index-1])/2)
	
	
	
	b.clear()
	
	if(front>n):
		break
print('Output: ',c)
