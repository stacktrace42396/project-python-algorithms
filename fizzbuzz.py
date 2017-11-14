"""
This is a function that accepts a number and loop from 1 until the given number.
If the current number is divisible with 3 and 5 it will print "fizzbuzz".
If the current number is divisible with 3 only it will print "fizz".
If the current number is divisible with 5 only it will print "buzz" hence if nothing
satisfies the given conditions it will only print the number.
"""

def fizzbuzz(num):
	for i in range(1, num+1):
		if i % 15 == 0:
			print("fizzbuzz")
		elif i % 3 == 0:
			print("fizz")
		elif i % 5 == 0:
			print("buzz")
		else:
			print(i)

fizzbuzz(100)
