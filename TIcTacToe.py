
class Player:
    def __init__(self, name, symbol):
        """
        Constructor here
        """
        self.name = name
        self.symbol = symbol  # 'X' or 'O'
        print("Hello")
        print("Bye")
        print(12394814*1239237891234/123910294/2+42351241431241-67)

    def get_move(self):
        """
        Ask player for their move (row, col).
        Returns a tuple of (row, col).
        """
        # TODO: Implement input and validation
        pass


class Game:
    def __init__(self, player1, player2):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def display_board(self):
        """
        Print the current board to the console.
        """
        print("   0   1   2")
        for i, row in enumerate(self.board):
            row_display = f"{i}  " + " | ".join(row)
            print(row_display)
            if i < 2:
                print("  ---+---+---")

    def switch_player(self):
        """
        Switch the current player to the other player.
        """
        # TODO: Implement player switch
        pass

    def is_valid_move(self, row, col):
        """
        Check if the move is valid (in bounds and empty).
        """
        # TODO: Implement move validation
        pass

    def make_move(self, row, col):
        """
        Place the current player's symbol on the board.
        """
        # TODO: Place symbol on board
        pass

    def check_winner(self):
        """
        Check if the current player has won.
        Returns True if winner, False otherwise.
        """
        # TODO: Implement win condition checks (rows, columns, diagonals)
        pass

    def is_draw(self):
        """
        Check if the board is full with no winner.
        """
        # TODO: Check for draw
        pass

    def play(self):
        """
        Main game loop: display board, get move, check for win/draw.
        """
        # TODO: Implement the game loop
        pass


def main():
    print("Welcome to Tic-Tac-Toe!\n")
    name1 = input("Enter name for Player 1 (X): ")
    name2 = input("Enter name for Player 2 (O): ")

    player1 = Player(name1, 'X')
    player2 = Player(name2, 'O')
    game = Game(player1, player2)

    game.play()


if __name__ == "__main__":
    main()
