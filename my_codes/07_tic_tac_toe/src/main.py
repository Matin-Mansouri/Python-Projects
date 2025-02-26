import random


class TicTacToe:
    """
    A class that represents the Tic Tac Toe game.
    """
    def __init__(self):
        """
        Initializes the game board and sets the first player randomly.
        """
        self.board: list[str] = [' '] * 10  # We use 1-9 for convenience, 0 is ignored
        self.player_turn: str = self.get_random_first_player()

    def get_random_first_player(self) -> str:
        """
        Randomly selects the first player ('X' or 'O').

        Returns:
            str: The player who will start the game.
        """
        return 'X' if random.randint(0, 1) == 0 else 'O'

    def fix_spot(self, cell: int, player: str) -> None:
        """
        Marks the specified cell on the board with the player's symbol.

        Args:
            cell (int): The cell number (1-9) to mark.
            player (str): The player ('X' or 'O') making the move.
        """
        self.board[cell] = player

    def has_player_won(self, player: str) -> bool:
        """
        Checks if the specified player has won the game.

        Args:
            player (str): The player ('X' or 'O') to check for a win.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),
                            (1, 5, 9), (3, 5, 7)]
        for combination in win_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == player:
                return True
        return False

    def is_board_filled(self) -> bool:
        """
        Checks if the game board is completely filled.

        Returns:
            bool: True if the board is filled, False otherwise.
        """
        return ' ' not in self.board

    def swap_player_turn(self) -> None:
        """
        Swaps the current player's turn.
        """
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'

    def show_board(self) -> None:
        """
        Prints the current state of the game board to the console.
        """
        print("\n")
        rows = [[self.board[i+j] for i in range(1, 4)] for j in range(0, 7, 3)]
        for row in rows:
            print(row)
        print("\n")

    def start(self) -> None:
        """
        Starts the Tic Tac Toe game loop.
        """
        while True:
            self.show_board()
            try:
                cell: int = int(input(f"Player {self.player_turn}, Enter the cell number: "))

                # Check if cell is in the allowed range and is empty
                if cell in range(1, 10) and self.board[cell] == ' ':
                    self.fix_spot(cell, self.player_turn)

                    if self.has_player_won(self.player_turn):
                        print(f"Player {self.player_turn} wins!")
                        break

                    if self.is_board_filled():
                        print("It's a Draw!")
                        break

                    self.swap_player_turn()

                else:
                    print("Invalid input, please try again.")
            except ValueError:
                print("Invalid input, please enter a number between 1 and 9.")


if __name__ == "__main__":
    # Create a game and start it
    game: TicTacToe = TicTacToe()
    game.start()