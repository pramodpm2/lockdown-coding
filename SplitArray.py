'''
Examples:

Input : arr[] = {12, 10, 5, 6, 52, 36}
k = 2
Output : arr[] = {5, 6, 52, 36, 12, 10}
Explanation : Split from index 2 and first
part {12, 10} add to the end .

Input : arr[] = {3, 1, 2}
k = 1
Output : arr[] = {1, 2, 3}
Explanation : Split from index 1 and first
part add to the end.
'''



a=[]
l=[]
n=int(input('Enter size: '))
k=int(input('enter k: '))
for i in range(0,n,1):
	a.append(int(input()))

l=a[:k]

for j in l:
		a.append(j)
print(a[k:])
