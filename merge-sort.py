def merge_sort(arr):
	if len(arr) < 2:
		return arr
	middle = len(arr) // 2	#	returns quotient without decimal point
	first_half = arr[:middle]
	second_half = arr[middle:]
	return merge(merge_sort(first_half), merge_sort(second_half))

def merge(first_half, second_half):
	result = []
	while len(first_half) and len(second_half):
		minimum = None
		if first_half[0] < second_half[0]:	#	change the less than to greater than to change in descending order
			minimum = first_half.pop(0)
		else:
			minimum = second_half.pop(0)
		result.append(minimum)

	if len(first_half):
		result += first_half
	else:
		result += second_half

	return result


print(merge_sort([6000, 34, 203, 3, 746, 200, 984, 198, 764, 1, 9, 1]))
print(merge_sort([100, -20, 40, -30, 16, -100, -101]))
