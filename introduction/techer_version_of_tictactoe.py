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