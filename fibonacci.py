#	O(2^n) complexity - not efficient
def fibonacci(position):
	#	base case
	if position < 3:
		return 1
	#	recursive case
	else:
		return fibonacci(position - 1) + fibonacci(position - 2)

print(fibonacci(6))
print(fibonacci(12))
print(fibonacci(20))
