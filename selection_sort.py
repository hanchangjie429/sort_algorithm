'''
selection sort
'''

def selection_sort(mylist):
	for i in range(0,len(mylist)):
		min_index=i
		min_value=mylist[i]
		for j in range(i,len(mylist)):
			if mylist[j]<min_value:
				min_value=mylist[j]
				min_index=j
		mylist[i],mylist[min_index]=mylist[min_index],mylist[i]
	
	return mylist

array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
print(selection_sort(array))
