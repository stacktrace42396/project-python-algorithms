"""
Longer version of is palindrome algorithm which uses array manipulation and list comprehension
of python.
"""

def is_palindrome(s):
	s_arr = [letter.lower() for letter in s if not letter == " "]
	valid_chars = list("abcdefghijklmnopqrstuvwxyz")
	
	valid_s_char = []

	for letter in s_arr:
		if valid_chars.index(letter) > -1:
			valid_s_char.append(letter)

	return "".join(valid_s_char) == "".join(list(reversed(valid_s_char)))


is_palindrome("race car")
