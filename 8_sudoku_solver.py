from pprint import pprint

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    row_values = puzzle[row]
    if guess in row_values:
        return False
    
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def solve_sudoku(puzzle):
    # step 1: choose a cell to make a guess
    row, col = find_next_empty(puzzle)
    if row is None:
        return True
    
    # step 2: if there is an empty spot, pick a guess
    for guess in range(1, 10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # step 4: recurse
            if solve_sudoku(puzzle):
                return True

        # step 5: if not valid or guess does not solve the puzzle, backtrack
        puzzle[row][col] = -1

    # step 6: if nothing works, it is unsolvable
    return False


if __name__ == '__main__':
    example_board = [
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
    print(solve_sudoku(example_board))
    pprint(example_board)