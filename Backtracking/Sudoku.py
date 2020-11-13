def check_valid(board):
    "Check if is a possible valid sudoku, not repeat element in rows, cols or squares, and values between 0 and 9, 0 is empty cell"
    validparameters = set([0,1,2,3,4,5,6,7,8,9])
    #Check rows
    for row in range(9):
        used_values = set()
        for col in range(9):
            if board[row][col] != 0 and board[row][col] in used_values or board[row][col] not in validparameters:
                return False
            used_values.add(board[row][col])
    
    #Check cols
    for col in range(9):
        used_values = set()
        for row in range(9):
            if board[row][col] != 0 and board[row][col] in used_values or board[row][col] not in validparameters:
                return False
            used_values.add(board[row][col])

    #Check squares
    for square in range(9):
        used_values = set()
        for row in range(3*(square//3),3*(square//3)+3):
            for col in range(3*(square%3),3*(square%3)+3):
                if board[row][col] != 0 and board[row][col] in used_values or board[row][col] not in validparameters:
                    return False
                used_values.add(board[row][col])
    return True

def check_empty(board):
    "If any cell is equal to 0 return False otherwise return True"
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return False
    return True

def solve(board):
    """Solves the sudoku without recursion, saves the positions that were at 0 in the variable changes and if it cannot continue, returns to the previous saved value.
    Finally check that it is well done, with the functions check_valid and check_empty."""

    changes = []
    row, col = 0, 0
    while row<9:
        while col<9:
            if board[row][col] == 0:
                board[row][col] +=1
                while not check_valid(board):
                    board[row][col]+=1
                    while board[row][col]>9:
                        board[row][col] = 0
                        if not changes:
                            return
                        row,col = changes.pop()
                        board[row][col] += 1
                    
                changes.append((row,col))
            col +=1
        row += 1
        col = 0       

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

solve(board)
print(check_empty(board))
print(check_valid(board))
print(board)