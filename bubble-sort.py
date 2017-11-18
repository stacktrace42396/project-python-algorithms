def bubble_sort(num_arr):
	#	return bubble sorted array
	for i in range(len(num_arr), -1, -1):
		for j in range(0, i-1, 1):
			if num_arr[j] > num_arr[j + 1]:
				temp = num_arr[j]
				num_arr[j] = num_arr[j + 1]
				num_arr[j + 1] = temp
	return num_arr

print(bubble_sort([5, 3, 8, 2, 1, 4]))
print(bubble_sort([20, 20, 31, 56, 1, 12, 12]))
print(bubble_sort([3, -9, -12, -1, 8]))
