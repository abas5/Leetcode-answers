# O(n^2) time and O(n) space
def longestPalindromicSubstring(string):
    # Write your code here.
	currentLongest = [0, 1] # start to end
	for i in range(1, len(string)):
		odd = getLongestPalindromeFrom(string, i - 1, i + 1)
		even = getLongestPalindromeFrom(string, i - 1, i)
		
		longest = max(odd, even, key = lambda x: x[1] - x[0])
		currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
		
	return string[currentLongest[0]:currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	return [leftIdx + 1, rightIdx]


string = "abaxyzzyxf"

print(string[3:9])
# print(longestPalindromicSubstring(string))

print(max([3,10], [3,9], key=lambda x: x[1] - x[0]))