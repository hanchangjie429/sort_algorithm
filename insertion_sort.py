'''
insertion sort

outer loop (1,length)
inner loop (i-1,-1,-1)
'''

def insertion_sort(mylist):
	for i in range(1,len(mylist)):
		for j in range(i-1,-1,-1):
			if mylist[j]>mylist[j+1]:
				mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
	return mylist
	
array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
print(insertion_sort(array))
