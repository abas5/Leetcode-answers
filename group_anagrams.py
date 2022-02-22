def groupAnagrams(words):
    # Write your code here.
    anagrams = {}
	
	for word in words:
		sortedWord = "".join(sorted(word))
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
			anagrams[sortedWord] = [word]
		
	return list(anagrams.values())

# log(n) since sorting Time and O(wn) space


# in python sorted() returns a list of sorted chars, ints
# while object.sort --> sorts it in place and returns nothing


def groupAnagrams(words):
    # Write your code here.
    # aaccbb and ccbbaa
	# aabbcc and aabbcc == we add both to the dict
	# aabbcc is the key and the word is the value, where value can be a list
	
	anagrams = {}
	
	for word in words:
		sorted_word = "".join(sorted(word))
		
		if sorted_word in anagrams:
			anagrams[sorted_word].append(word)
		else:
			anagrams[sorted_word] = [word]
	
	return list(anagrams.values())