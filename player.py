class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        while True:
            try:
                row = int(input(f'{self.name}, enter the row (0-2): '))
                col = int(input(f'{self.name}, enter the column (0-2): '))
                return row, col
            except ValueError:
                print('Invalid input. Please enter numbers.')
