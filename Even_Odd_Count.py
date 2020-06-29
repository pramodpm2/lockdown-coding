'''
Given a list of numbers, write a Python program to count Even and Odd numbers in a List. 
Example: Input: list1 = [2, 7, 5, 64, 14] Output: Even = 3, odd = 2 Input: list2 = [12, 14, 95, 3] Output: Even = 2, odd = 2 Example 1: count Even and Odd numbers from given list using for loop Iterate each element in the list using for loop and check if num % 2 == 0, the condition to check even numbers. If the condition satisfies, then increase even count else increase odd count.
'''
n=int(input('Enter The Size Of List: '))
print('Enter The List Elements: ')
a=[]
oc=0
ec=0
for i in range(0,n):
	a.append(int(input()))
for i in a:
	if i%2==0:
		 ec+=1
	else:
		oc+=1

print('Total Even Numbers In a List: ',ec)
print('Total Odd Numbers In a List: ',oc)
