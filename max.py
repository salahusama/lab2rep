def max(array):
	max = array[0]
	for num in array:
		if num > max:
			max = num
	return max

myArray = [1, 3, 5, 12, 2, 56]
print(myArray)
print( "MAX: ", max(myArray))
