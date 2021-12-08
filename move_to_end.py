def moveElementToEnd(array, toMove):
    # Write your code here.
    left_pointer = 0
	right_pointer = len(array) - 1
	
	while left_pointer < right_pointer:
		# Handle the case where you start w/ further non toMove element
		while left_pointer < right_pointer and array[right_pointer] == toMove:
			right_pointer -= 1
		if array[left_pointer] == toMove:
			array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]

		left_pointer += 1
	
	return array