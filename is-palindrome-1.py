"""
This function accepts a string and returns TRUE if the given string is the same when
it was spelled backwards and FALSE if it is not.
This function uses string manipulation of python.
"""

def is_palindrome(s):
	return s.lower() == s[::-1].lower()


print(is_palindrome("racecar"))
