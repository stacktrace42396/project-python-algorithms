"""
This function accepts a given string as a parameter and each word in that given string will be
return in their inverse form. For efficiency it also uses a string manipulation built in python
and for loop to loop through the given string.
"""

def reverse_words(given_text):
	words_arr = given_text.split(" ")
	reverse_arr = []

	for word in words_arr:
		reverse_str = word[::-1]
		reverse_arr.append(reverse_str)

	return " ".join(reverse_arr)


print(reverse_words("this is an example string"))
