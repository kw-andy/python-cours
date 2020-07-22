'''
Given a stream of unsorted integers, find the median element 
in sorted order at any given time. So, we will be receiving a 
continuous stream of numbers in some random order 
and we don’t know the stream length in advance. 
Write a function that finds the median of the already 
received numbers efficiently at any time. 
We will be asked to find the median multiple times. 
Just to recall, median is the middle element in an odd length sorted array, 
and in the even case it’s the average of the middle elements.
'''

from statistics import median

def med_integ(lis_of_integ):
	sort_lst = sorted(lis_of_integ)
	med_num = median(sort_lst) 
	return med_num

print(med_integ([1,1,3,4,5,5,6,10,12]))	
print(med_integ([1,1,3,4,5,8,7,10,200,32]))	