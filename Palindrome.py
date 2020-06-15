'''

A string is k palindrome if it can be transformed into a palindrome on removing at most k characters from it. Your task is to complete the function is_k_palin which takes two arguments a string str and a number N . Your function should return true if the string is k palindrome else it should return false.

Input:
The first line of input is an integer T denoting the number of test cases . Then T test cases follow . Each test case contains a string str and an integer N separated by space.

Output:
The output will be 1 if the string is k palindrome else 0 .

Example
Input : String - abcdecba, k = 1
Output : Yes
String can become palindrome by remo-
-ving 1 character i.e. either d or e)

Input : String - abcdeca, K = 2
Output : Yes
Can become palindrome by removing
2 characters b and e.

Input : String - acdcb, K = 1
Output : No
String can not become palindrome by
removing only one character.
'''



a=input('Enter A Main String: ')
k=int(input('Enter K Value: '))

for i in a:
	count=a.count(i)
	if (count==1):
		a=a.replace(i,'')
		k=k-1
		if(k==0):
			break
	count=0

p=a[::-1]


if(p==a):
	print('Yes')
else:
	print('No')
