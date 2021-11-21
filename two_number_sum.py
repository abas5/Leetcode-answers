# Leetcode Question Two Number Sum
def twoNumberSum(array, targetSum):
    # Write your code here.
	# traversing the array and adding each element to another element in the arrray
	for index, number in enumerate(array):
		print(index)
		# array == [1,2,3,4]
		# number = 1
		# Create another loop that skips the current index of the first loop. Then add each element after it and check if it matches the target sum

		for secondNum in array[index+1:]:
			print("array: %s" % array[index+1:])
			if targetSum == number + secondNum:
				return [number, secondNum]
	return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
