def get_mean(arr):
	n_sum = 0
	
	for num in arr:
		n_sum += num

	return n_sum / len(arr)


def get_median(arr):
	arr = sorted(arr)
	median = None
	if len(arr) % 2 != 0:
		median = arr[math.floor(len(arr)/2)]
	else:
		num1 = arr[int((len(arr)/2) - 1)]
		num2 = arr[int(len(arr)/2)]
		median = (num1+num2)/2
	return median


def get_mode(arr):
	mode_obj = dict()

	for num in arr:
		if num not in mode_obj:
			mode_obj[num] = 1
		else:
			mode_obj[num] += 1

	max_frequency = 0
	modes = []

	for num in mode_obj:
		if mode_obj[num] > max_frequency:
			modes = [num,]
			max_frequency = mode_obj[num]
		elif mode_obj[num] == max_frequency:
			modes.append(num)

	if len(modes) == len(mode_obj):
		modes = []

	return modes


def mean_median_mode(arr):
	return {
		"mean": get_mean(arr),
		"median": get_median(arr),
		"mode": get_mode(arr),
	}


print(mean_median_mode([9, 10, 23, 10, 23, 9]))
print(mean_median_mode([1, 2, 3, 4, 5, 4, 6, 1]))
