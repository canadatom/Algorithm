#!/usr/bin/python

def quicksort(array, start, finish):
	if (start < finish):
		pivot_index = partition(array, start, finish)
		print "pivot_index: " + str(pivot_index)
		quicksort(array, start, pivot_index - 1)
		quicksort(array, pivot_index + 1, finish)

	return array

def partition(array, start, finish):
	pivot = array[finish]
	p_index = start

	print str(p_index) + " " + str(pivot) 

	for i in range(start, finish):
		if array[i] <= pivot:
			array[p_index], array[i] = array[i], array[p_index]
			p_index += 1
			
	array[p_index], array[finish]  = array[finish], array[p_index]

	return p_index

array = [9, 2, 3, 10, 8, 4, 7, 6, 5, 1]
print quicksort(array, 0, len(array) - 1)
