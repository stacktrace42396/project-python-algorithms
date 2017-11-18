def sieve_of_eratosthenes(num):
	#	return all prime numbers up to num in an array
	primes = []
	non_primes = []
	for i in range(2, num+1):
		if i not in non_primes:
			primes.append(i)
			for j in range(i*i, num+1, i):
				non_primes.append(j)
	return primes

print(sieve_of_eratosthenes(10))
print(sieve_of_eratosthenes(20))
print(sieve_of_eratosthenes(100))
