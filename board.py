class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        print('---------')
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(f' {cell} |', end='')
            print('\n---------')

    def is_full(self) -> bool:
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def is_winner(self, player) -> bool:
        symbol = player.symbol
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == symbol:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == symbol:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True
        return False

    def is_valid_move(self, move) -> bool:
        row, col = move
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            return True
        return False

    def make_move(self, move, player) -> bool:
        if self.is_valid_move(move):
            row, col = move
            self.board[row][col] = player.symbol
            return True
        return False
