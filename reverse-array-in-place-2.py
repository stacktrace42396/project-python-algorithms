"""
This function accepts an array as a parameter and returns the reverse of it.
It uses for loop and some simple math equation to swap all values inside the array.
"""

def reverse_array_in_place(arr):
	
	for num in range(0, int(len(arr)/2)):
		temp = arr[num]
		arr[num] = arr[len(arr) - 1 - num]
		arr[len(arr) - 1 - num] = temp

	return arr


print(reverse_array_in_place([1,2,3,4,5]))
