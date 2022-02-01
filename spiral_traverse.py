


array = [[1, 2, 3, 4],
		 [5, 6, 7, 8],
		 [9, 10, 11, 12],
		 [13 ,14, 15, 16]
		  ]
			

start_row, end_row = 0, len(array) - 1
start_col, end_col = 0, len(array[0]) - 1


for i in range(0, 5):
	print("Hello")

while start_row <= end_row and start_col <= end_col:
	for col in range(start_col, end_col + 1):
		print(array[start_row][col])
	
	for row in range(start_row + 1, end_row + 1):
		print(array[row][end_col])
	
	for col in reversed(range(start_col, end_col)):
		print(array[end_row][col])
	
	for row in reversed(range(start_row + 1, end_row)):
		print(array[row][start_col])
	
	
	start_col += 1
	end_col -= 1
	start_row += 1
	end_row -= 1