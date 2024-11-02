class TicTacToePosition:
    def __init__(self, board):
        self.board = board

    def top_left(self):
        return self.board[0]

    def top_middle(self):
        return self.board[1]

    def top_right(self):
        return self.board[2]

    def middle_left(self):
        return self.board[3]

    def middle_middle(self):
        return self.board[4]

    def middle_right(self):
        return self.board[5]

    def bottom_left(self):
        return self.board[6]

    def bottom_middle(self):
        return self.board[7]

    def bottom_right(self):
        return self.board[8]

    def __str__(self):
        return f"{self.top_left()}{self.top_middle()}{self.top_right()}\n{self.middle_left()}{self.middle_middle()}{self.middle_right()}\n{self.bottom_left()}{self.bottom_middle()}{self.bottom_right()}"

    def is_winner(self, a, b, c):
        if winner(a, b, c):
            return True
        else:
            return False

    def is_winner_overall(self):
        return (self.is_winner(self.top_left(), self.top_middle(), self.top_right()) or
                    self.is_winner(self.middle_left(), self.middle_middle(), self.middle_right()) or
                    self.is_winner(self.bottom_left(), self.bottom_middle(), self.bottom_right()) or
                    self.is_winner(self.top_left(), self.top_middle(), self.top_right()) or
                    self.is_winner(self.middle_left(), self.middle_middle(), self.middle_right()) or
                    self.is_winner(self.bottom_right(), self.bottom_middle(), self.bottom_right()) or
                    self.is_winner(self.top_left(), self.middle_middle(), self.bottom_right()) or
                    self.is_winner(self.top_right(), self.middle_middle(), self.bottom_left())
                )

    def is_position_full(self, position):
        return self.board[position] == "O" or self.board[position] == "X"
    def is_board_full(self):
        for i in range(9):
            if is_position_full(i):
                return False
        return True

my_position = TicTacToePosition("XOXOXOXOX")
print(my_position)
print(my_position.middle_middle())
print(my_position.is_winner_overall())


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
    if a == b and b == c:
        return True
    else:
        return False

def whosSame(a, b, c):
    if a == b and b == c:
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
    print(f"{top_left}{top_middle}{top_right}\n{middle_left}{middle_middle}{middle_right}\n{bottom_left}{bottom_middle}{bottom_right}")


drawBoard(123456789)
print(isWin("123456789"))
