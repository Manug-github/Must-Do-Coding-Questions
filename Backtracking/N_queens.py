def check_valid(board):
    "Check if is a possible queens distribution, max one queen per row, column or diagonal"
    # Check rows
    for row in range(len(board)):
        if sum(board[row])>1:
            return False
    # Check Cols
    for col in range(len(board)):
        ans = 0
        for row in range(len(board)):
            ans += board[row][col]
        if ans>1:
            return False
    # Check Diagonals
    N = len(board)
    for diag in [[board[y-x][x] for x in range(N) if 0<=y-x<N] for y in range(2*N-1)]:
        if sum(diag)>1:
            return False
    for diag in [[board[N-1-y+x][x] for x in range(N) if 0<=y-x<N] for y in range(2*N-1)]:
        if sum(diag)>1:
            return False

    return True


def solve(board):
    """Solves the NQueens problem, save the position of the queens and if it is not possible to put a queen in that row, move the one that has been placed previously.
    Finally check that it is well done, with the functions check_valid and check_empty."""
    if len(board)!=len(board[0]) or not check_valid(board):
        return
    changes = []
    N = len(board)
    row, col = 0, 0
    while row<N:
        while col<N:
            if sum(board[row])==0:
                board[row][col] = 1
                while not check_valid(board):
                    board[row][col]= 0
                    col += 1
                    while col==N:
                        if not changes: # If not previous Queen, ends.
                            return
                        row,col = changes.pop()
                        board[row][col] = 0
                        col+=1
                    board[row][col] = 1
                changes.append((row,col))
            col +=1
        row += 1
        col = 0  

board = [
        [0,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,1,0,0,0,0,0],
        ]

board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        ]

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        ]

solve(board)

if check_valid(board) and sum([sum(board[x]) for x in range(len(board))]) == max(len(board),len(board[0])):
    for row in board:
        print(row)
else:
    print("No valid input")