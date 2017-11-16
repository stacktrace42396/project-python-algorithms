import math

def binary_search(num_array, num_key):
	num_array = sorted(num_array)
	mid_index = math.floor(len(num_array)/2)
	mid_elem = num_array[mid_index]
	
	if mid_elem == num_key:
		return True
	elif mid_elem < num_key and len(num_array) > 1:
		return binary_search(num_array[mid_index:len(num_array)], num_key)
	elif mid_elem > num_key and len(num_array) > 1:
		return binary_search(num_array[0:mid_index], num_key)
	else:
		return False

print(binary_search([5, 7, 12, 16, 36, 39, 42, 56, 71], 56))
print(binary_search([5, 7, 12, 16, 36, 39, 42, 56, 71], 7))
