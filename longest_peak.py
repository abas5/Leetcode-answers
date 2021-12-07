def longestPeak(array):
    # Write your code here.
    longestPeakLength = 0
	i = 1 # start at 1 b/c need a less than and greater than adjecent
	
	while i < len(array) - 1:
		isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
		
		if not isPeak:
			i += 1
			continue
		
		# No longer need to explore the items in the current peak so start
		# at the end of the peak
		leftIdx = i - 2 # we already kn i -1 is less than i
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
			leftIdx -= 1
		
		rightIdx = i + 2
		while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
			rightIdx += 1
			
		currentPeakLength = rightIdx - leftIdx - 1
		longestPeakLength = max(longestPeakLength, currentPeakLength)
		i = rightIdx
		
	return longestPeakLength
