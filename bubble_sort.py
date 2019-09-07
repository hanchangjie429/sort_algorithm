'''
三步搞定冒泡排序

1. 弄清楚外循环次数
外循环次数等于 数组长度-1
2. 弄清楚内循环次数
内循环次数等于 列表长度-1-外循环计数
3. 弄清楚换值条件
换值条件为前一个数大于（或小于，取决于你的冒泡排序是顺序还是逆序）后一个数


list=[4,5,1,3]

outer loop: i = 0 to n-1
	inner loop: j = 0 to n-1-i

'''



def bubbleSort(mylist):
	for i in range(0,len(mylist)-1): # outer loop
		for j in range(0,len(mylist)-i-1): # inner loop
			if mylist[j]>mylist[j+1]: # swap case
				mylist[j],mylist[j+1]=mylist[j+1],mylist[j] # swap
	return mylist


array = [5, 6, -1, 4, 2, 8, 10, 7, 6, 0, 101, -102]
print(bubbleSort(array))



