def nPr(n,r):
	return (fact(n)/(fact(n-r)))

def fact(n):
	res=1
	
	for i in range(2,n+1):
		res=res*i
	return res
a=0
t=int(input())
while(t>0):
	n=int(input())
	r=int(input())
	
	if n>r:
		a=nPr(n,r)
		print(a)
		
	else:
		print('R value Shoud Be Less Than N')
	t-=1
	
