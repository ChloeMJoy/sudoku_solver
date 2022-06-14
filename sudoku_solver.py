def find_next_empty(puzzle):
    #finds next row, col on the puzzle not yet filled --> rep with -1
    #returns row, col tuple (or (None, None) if there is none)

    #0-8 for our indicies
    for r in range(9):
        for c in range (9): #range (9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c
    return None, None #if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at row/col is valid guess
    #returns True if valid, False otherwise

    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #Square
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    for r in range(row_start, row_start +3):
        for c in range(col_start, col_start +3):
            if puzzle[r][c] == guess:
                return False
    return True


    

def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    #puzzle is a list of lists, each inner list is a row in the puzzle
    #returns whether a solution exists
    
    #step 1: Choose a place to make a guess
    row, col = find_next_empty(puzzle)

    #step 1.1: If there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True
    #step 2: If place to guess, make a guess between 1 and 9
    for guess in range(1, 10): #range (1,10) is 1, 2, 3, ... 9
        #step 3: Check if valid guess
        if is_valid(puzzle, guess, row, col):
            #step 3.1: if guess is valid, place guess
            puzzle[row][col] = guess
            # now recurse using puzzle
            #step 4: Recursively call our function 
            if solve_sudoku(puzzle):
                return True
        #step 5: if not valid OR if guess doesn't solve puzzle
        puzzle[row][col] = -1 #reset the guess
    #step 6: if none of the numbers work, the puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [-1,-1,-1, -1,-1,7, -1,8,1],
        [5,-1,-1, -1,-1,4, -1,-1,-1],
        [-1,2,-1, -1,-1,3, -1,-1,-1],

        [-1,8,-1, -1,-1,-1, -1,7,3],
        [-1,6,-1, -1,-1,-1, -1,-1,-1],
        [-1,-1,4, 5,6,-1, 2,-1,-1],

        [4,-1,-1, 8,-1,-1, -1,1,7],
        [-1,1,-1, -1,-1,-1, -1,-1,-1],
        [-1,-1,-1, -1,9,-1, -1,2,-1],
    ]
    print(solve_sudoku(example_board))
    print(example_board)