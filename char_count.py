def generateDocument(characters, document):
    # Write your code here.
    
	for i in range(len(document)):
		letter_count_doc = document.count(document[i])
		letter_count_characters = characters.count(document[i])
		
		if letter_count_doc <= letter_count_characters:
			continue
		else:
			return False
		
	return True
