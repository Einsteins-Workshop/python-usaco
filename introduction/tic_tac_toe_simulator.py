def whoWon(board):
    board=str(board)
    if whosSame(board[0], board[1], board[2])!=None:
        return board[0]
    if whosSame(board[3], board[4], board[5])!=None:
        return board[3]
    if whosSame(board[6], board[7], board[8])!=None:
        return board[6]
    if whosSame(board[0], board[3], board[6])!=None:
        return board[0]
    if whosSame(board[1], board[4], board[7])!=None:
        return board[1]
    if whosSame(board[2], board[5], board[8])!=None:
        return board[2]
    if whosSame(board[0], board[4], board[8])!=None:
        return board[0]
    if whosSame(board[2], board[4], board[6])!=None:
        return board[2]

def isWin(board):
    board = str(board)
    if isSame(board[0], board[1], board[2]) or isSame(board[3], board[4], board[5]) or isSame(board[6], board[7], board[8]) or isSame(board[0], board[3], board[6]) or isSame(board[1], board[4], board[7]) or isSame(board[2], board[5], board[8]) or isSame(board[0], board[4], board[8]) or isSame(board[2], board[4], board[6]):
        return True
    else:
        return False

def isSame(a, b, c):
    if a == b and b == c and a!="_":
        return True
    else:
        return False

def whosSame(a, b, c):
    if a == b and b == c and a!="_":
        return a
    else:
        return None

def drawBoard(board):
    board = str(board)
    top_left = board[0]
    top_middle = board[1]
    top_right = board[2]
    middle_left = board[3]
    middle_middle = board[4]
    middle_right = board[5]
    bottom_left = board[6]
    bottom_middle = board[7]
    bottom_right = board[8]
    print(f"{top_left}|{top_middle}|{top_right}\n-----\n{middle_left}|{middle_middle}|{middle_right}\n-----\n{bottom_left}|{bottom_middle}|{bottom_right}")

def findPossiblities(board, turn, turnsRemaining):
    if isWin(board):
        print(whoWon(board))
        drawBoard(board)
        return whoWon(board)
    board = str(board)
    if turn=="x":
        nextTurn="o"
    else:
        nextTurn="x"
    for i in range(turnsRemaining):
        newBoard=board
        if newBoard[i]=="_":
            newBoard=newBoard[:i]+turn+newBoard[i+1:]
            findPossiblities(newBoard, nextTurn, turnsRemaining-1)

findPossiblities("_________", "x", 9)