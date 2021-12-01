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