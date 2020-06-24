'''
We follow this algorithm.

Create a temporary stack say tmpStack.
While input stack is NOT empty do this:
• Pop an element from input stack call it temp
• while temporary stack is NOT empty and top of temporary stack is greater than temp,
pop from temporary stack and push it to the input stack
• push temp in temporary stack
The sorted numbers are in tmpStack
'''


a=[34,3,31,98,92,23]
t=[]
ele=0
val=0
while(len(a)!=0):
	ele=a.pop()
	print('Poped Element Is: ',ele)
	print('Input Stack Is: ',a)
	while(len(t)!=0 and ele<t[-1]):
	  	val=t.pop()
	  	a.append(val)
	t.append(ele)
	print('Temp_stack Is',t)
	print('')
