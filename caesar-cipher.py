"""
Caesar Cipher algorithm:
This function accepts a string and number parameter which will transform the given string into
a new string that is shifted by the given number for each letter.
"""


def caesar_cipher(given_string, num):
	num = num % 26
	lower_text = given_string.lower()
	alpha_arr = list("abcdefghijklmnopqrstuvwxyz")
	new_text = ""

	for letter in lower_text:
		current_letter = letter
		if current_letter == " ":
			new_text += current_letter
			continue
		current_index = alpha_arr.index(current_letter)
		new_index = current_index + num
		
		if new_index > 25:
			new_index = new_index - 26

		if new_index < 0:
			new_index = 26 + new_index

		if given_string[lower_text.index(letter)].isupper():
			new_text += alpha_arr[new_index].upper()
		else:
			new_text += alpha_arr[new_index]

	return new_text



print(caesar_cipher("Zoo Keeper", 2))
print(caesar_cipher("Big Car", -16))
print(caesar_cipher("Javascript", -900))
