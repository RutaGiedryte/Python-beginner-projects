import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted += 1

        return board
    
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighbor_bombs(r, c)
    
    def get_num_neighbor_bombs(self, row, col):
        num_neighbors = 0

        for r in range(max(0, row - 1), min(self.dim_size, (row+1) + 1)):
            for c in range(max(0, col - 1), min(self.dim_size, (col+1) + 1)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighbors += 1

        return num_neighbors

    def dig(self, row, col):
        # return False if bomb dug, True else
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row - 1), min(self.dim_size, (row+1) + 1)):
            for c in range(max(0, col - 1), min(self.dim_size, (col+1) + 1)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True


    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r, c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                else:
                    visible_board[r][c] = ' '
        
        
        string_rep = ''
        # this part is just copied from already finished code, it formats the string
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        # end of copied code
        return string_rep
                    


def play(dim_size = 10, num_bombs = 10):
    # 1. Create the board, plant bombs
    board = Board(dim_size, num_bombs)

    # 2. Show the board, get user's move
    # 3. a) If location is a bomb,, show "game over"
    # 3. b) If not, dig recursively
    # 4. Repeat 2 and 3
    safe = True

    while(len(board.dug)) < board.dim_size**2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? input as 'row,col'. "))
        row, col = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
            print("Invalid location, try again")
            continue
        safe = board.dig(row, col)
        if not safe:
            break
    
    if safe:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost!")
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
    print(board)


if __name__ == '__main__':
    play()