def runLengthEncoding(string):
    # Write your code here.
	current_char = string[0]
	run_length = 1
	encoded_string = ""

	for index in range(1, len(string)):
		if current_char != string[index] or run_length == 9:
			encoded_string = "%s%s%s" % (encoded_string, current_char, run_length)
			current_char = string[index]
			print(current_char)
			print(string)
			print(index)
			print(string[index])
			run_length = 1
		run_length += 1

	print(encoded_string)
	return encoded_string



runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")