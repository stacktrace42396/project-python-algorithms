"""
This is a function that takes a note and a magazine texts as a parameter.
It returns true if the note given is possible to make with the given magazine text
and false if it is not possible.
"""

def harmless_ransom_note(note_text, magazine_text):
	note_arr = note_text.lower().split()
	magazine_arr = magazine_text.lower().split()

	magazine_obj = dict()

	#	creates an object that stores the number of times the word occured in magazine text
	for word in magazine_arr:
		if word not in magazine_obj:
			magazine_obj[word] = 1
		else:
			magazine_obj[word] += 1

	#	checks if given note text is possible to make with the given magazine text
	for word in note_arr:
		if word in magazine_obj:
			magazine_obj[word] -= 1
			if magazine_obj[word] < 0:
				return False
		else:
			return False
	
	return True


print(harmless_ransom_note("this this is magazine paragraph",
	"this is an example magazine paragraph to test magazine random note"))
