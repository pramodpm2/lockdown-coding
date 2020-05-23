'''
ProgramProgram To Print Triangular Number Series Till n
'''

n=int(input('Enter Number '))
a=n
l=1
for i in range(n,0,-1):
	for j in range (a,0,-1):	
		print(end=' ')
	
	for p in range(0,l,1):
		print('*',end=' ')
		if(l-1==n):
			break
	l=l+1
	print()
	a=a-1
