num_cache = {}

def mem_fibonacci(position):
	if type(position) != int:
		raise TypeError("position must be an integer.")

	if position < 1:
		raise ValueError("position must be positive number.")

	if position in num_cache:
		return num_cache[position]

	else:
		if position < 3:
			return 1
		else:
			num_cache[position] = mem_fibonacci(position-1) + mem_fibonacci(position-2)
		return num_cache[position]


print(mem_fibonacci(999))
	
