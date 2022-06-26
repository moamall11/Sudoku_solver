def _find_empty_spot(puzzle):
	"""returns row,column for an empty spot on the puzzle
	and returns None,None when there is no empty spots on the puzzle"""
	for r in range(9):
		for c in range(9):
			if puzzle[r][c]==-1:
				return r,c
	return None,None

def _is_valid(puzzle,row,col,guess):
	"""returns True when the guess is valid else False"""
	#we have to check all the possibilities for our guess to be wrong.
	#check the row.
	if guess in puzzle[row]:
		return False
	#check the column.
	if guess in [puzzle[i][col] for i in range(9)]:
		return False
	#check the square.
	start_row = (row // 3) * 3
	start_col = (col // 3) * 3
	for r in range(start_row,start_row + 3):
		for c in range(start_col,start_col + 3):
			if puzzle[r][c] == guess:
				return False
	#if it didn't return False then the guess is valid.
	return True


def solve_sudoku(puzzle):
	"""solves the sudoku puzzle"""
	#get an empty spot.
	row,col=_find_empty_spot(puzzle)

	#when there are no empty spots -> puzzle solved(win).
	if row is None:
		return True
	#try all the numbers(1-9) until it finds a valid number 
	#to add to the puzzle.
	for guess in range(1,10):
		if _is_valid(puzzle,row,col,guess):
			puzzle[row][col] = guess
			#after applying each guess we will play the whole game 
			#and see the results. 
			#(if it results in a win then the guess is right)
			if solve_sudoku(puzzle):
				return True
		#if the guess is invalid or doesn't result in a win 
		#then reset the guess to -1 (empty spot) 
		#so we can try another guess 
		#(so it doesn't change the result of the right guess).
		puzzle[row][col]=-1
	#if all the combinations couldn't solve the puzzle then it's unsolvable.
	return False


if __name__=='__main__':
	# puzzle=[[-1 for _ in range(9)] for _ in range(9)]
	puzzle=[
	[3, 9, -1,   -1, 5, -1,   -1, -1, -1],
	[-1, -1, -1,   2, -1, -1,   -1, -1, 5],
	[-1, -1, -1,   7, 1, 9,   -1, 8, -1],

	[-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
	[2, -1, 6,   -1, -1, 3,   -1, -1, -1],
	[-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

	[5, -1, -1,   -1, -1, -1,   -1, -1, -1],
	[6, 7, -1,   1, -1, 5,   -1, 4, -1],
	[1, -1, 9,   -1, -1, -1,   2, -1, -1]
	]
	result=solve_sudoku(puzzle)
	if result:
		print("solved!")
	else:
		print("couldn't solve it, it's unsolvable!")
	for r in puzzle:
		print(r)



	

