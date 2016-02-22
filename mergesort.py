#!/usr/bin/python

def merge(leftArray, rightArray):

	i = 0 # left
	j = 0 # right 
	k = 0 # new array
	array = []

	while i < len(leftArray) and j < len(rightArray):
		if leftArray[i] < rightArray[j]:
			array[k] = leftArray[i]
			i += 1
		else:
			array[k] = rightArray[j]
			j += 1
		k += 1

	while i < len(leftArray):
		array[k] = leftArray[i]
		i += 1
		k += 1

	while j < len(rightArray):
		array[k] = rightArray[j]
		j += 1
		k += 1
	print("Merging ",array)
	return array

def mergeSort(array):
	print ("Splitting", array)
	# divide 
	if len(array) <= 1:
		return array

	mid = len(array) // 2
	leftArray = array[:mid]
	rightArray = array[mid:]
	mergeSort(leftArray)
	mergeSort(rightArray)
		
	i = 0 # left
	j = 0 # right 
	k = 0 # new array
	#array = []

	while i < len(leftArray) and j < len(rightArray):
		if leftArray[i] < rightArray[j]:
			array[k] = leftArray[i]
			i += 1
		else:
			array[k] = rightArray[j]
			j += 1
		k += 1

	while i < len(leftArray):
		array[k] = leftArray[i]
		i += 1
		k += 1

	while j < len(rightArray):
		array[k] = rightArray[j]
		j += 1
		k += 1
	print("Merging ",array)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)