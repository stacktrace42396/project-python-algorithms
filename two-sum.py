def two_sum(num_array, n_sum):
	pairs_arr = []
	hash_table = []

	for num in num_array:
		current_num = num
		counter_num = n_sum - current_num
		if counter_num in hash_table:
			pairs_arr.append([current_num, counter_num])
		hash_table.append(current_num)

	return pairs_arr

print(two_sum([1, 6, 4, 5, 3, 3], 7))
print(two_sum([40, 11, 19, 17, -12], 28))
