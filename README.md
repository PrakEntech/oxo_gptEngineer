Based on the requirements, here are the core classes, functions, and methods that will be necessary for the text-based tic tac toe game:

1. `Board` class:
   - `__init__(self)`: Initializes the game board.
   - `display(self)`: Displays the current state of the board.
   - `is_full(self) -> bool`: Checks if the board is full.
   - `is_winner(self, player) -> bool`: Checks if a player has won.
   - `is_valid_move(self, move) -> bool`: Checks if a move is valid.
   - `make_move(self, move, player) -> bool`: Makes a move on the board.

2. `Player` class:
   - `__init__(self, name, symbol)`: Initializes a player with a name and symbol.
   - `get_move(self) -> Tuple[int, int]`: Gets the move from the player.

3. `Game` class:
   - `__init__(self, player1, player2)`: Initializes the game with two players.
   - `play(self)`: Starts the game and handles the game flow.

Now, let's proceed with the implementation of the code.

**board.py**
