n=int(input('Enter The Number: '))
rev=0
a=0
while n>0:
	a=n%10
	rev=rev*10+a
	n=n//10
print('Thr Revers Number Is: ',rev)
	
