'''
Given two lists, sort the values of one list using the second list 

Examples:
Input :
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"] list2 = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]
Output :
['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g'] Input : list1 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"] list2 = [ 0, 1, 1, 0, 1, 2, 2, 0, 1] Output : ['g', 'k', 'r', 'e', 'e', 'g', 's', 'f', 'o']
'''
list1=['a' ,'b','c','d','e','f','g','h']
list2=[0,1,1,0,2,2,0,1]

Z = [x  for _,x in sorted(zip(list2,list1))]
print('Output: ',
