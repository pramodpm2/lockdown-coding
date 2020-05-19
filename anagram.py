count=0
string1=input('Enter 1st string : ')
string2=input('Enter the 2nd string: ')
n1=len(string1)
n2=len(string2)
if n1!=n2:
	print('Given strings are not angram to each other')
else:
    a=sorted(string1)
    b=sorted(string2)
    for i in range(0,n1):
    	if a[i]==b[i]:
    		count+=1
    	else:
    		print('Given strings are not angram to each other')
    		break
if(n1==count):
	print('The given strings are angram to each other')
