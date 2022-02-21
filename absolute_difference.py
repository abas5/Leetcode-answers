def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    # array_one = [-1, 5, 10, 20, 28, 3]
	# array_two = [26, 134, 135, 15, 17, -2]
	# output = [28, 26]
	# have a equation that calcaultes the abosulte difference
	# 26 - (-1) = 27
	# 26 - 5 = 21 # we flipped and subtracted by the 2nd element which was bigger
	# 1st condition: if element in array2 is bigger than element in array1 then
	# subtract by element 2
	# 28 - 15 = 13
	# -1 - (-2) = 1
	min_value = 99999999999
	min_pairs = None
	
	for one in arrayOne:
		for two in arrayTwo:
			if two > one:
				ans = two - one
				if ans < min_value:
					min_value = ans
					min_pairs = [one, two]
			else:
				ans = one - two
				if ans < min_value:
					min_value = ans
					min_pairs = [one, two]
	
	return min_pairs