from board import Board
from player import Player


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player = player1

    def play(self):
        while not self.board.is_full() and not self.board.is_winner(self.current_player):
            self.board.display()
            move = self.current_player.get_move()
            if self.board.make_move(move, self.current_player):
                if self.board.is_winner(self.current_player):
                    self.board.display()
                    print(f'{self.current_player.name} wins!')
                    return
                self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
            else:
                print('Invalid move. Try again.')
        self.board.display()
        print('It\'s a tie!')


if __name__ == '__main__':
    player1 = Player('Player 1', 'X')
    player2 = Player('Player 2', 'O')
    game = Game(player1, player2)
    game.play()
