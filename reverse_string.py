# O(n) time O(n) space
def reverseWordsInString(string):
    words = []
	start_of_word = 0
	
	for idx in range(len(string)):
		character = string[idx]

		if character == " ":
			words.append(string[start_of_word:idx])
			start_of_word = idx
		elif string[start_of_word] == " ":
			words.append(" ")
			start_of_word = idx
		
	words.append(string[start_of_word:])
	
	reverseList(words)
	
	return "".join(words)

def reverseList(list):
	start, end = 0, len(list) - 1
	
	while start < end:
		list[start], list[end] = list[end], list[start]
		start += 1
		end -= 1