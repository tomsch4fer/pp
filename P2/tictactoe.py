"""Tom Schäfer, Erik Gladitz FPP WS23/24"""

class TicTacToe:
    # nur eine Klasse ist nicht objektorientiert -> player, board, 
    def __init__(self):
        self.board = [['--', '--', '--'],
                      ['--', '--', '--'],
                      ['--', '--', '--']]
        self.current_player = 'Player 1'

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def make_move(self, row, col):
        if self.board[row - 1][col - 1] == '--':
            self.board[row - 1][col - 1] = 'X' if self.current_player == 'Player 1' else 'O'
        else:
            print("Feld bereits belegt. Bitte erneut versuchen.")

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != '--':
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '--':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '--':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '--':
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if '--' in row:
                return False
        return True

    def play(self):
        print("Willkommen bei TicTacToe")
        self.print_board()

        while True:
            print(f"{self.current_player} ist an der Reihe")
            try:
                row = int(input("Bitte Zeile eingeben: "))
                col = int(input("Bitte Spalte eingeben: "))
                if 1 <= row <= 3 and 1 <= col <= 3:
                    self.make_move(row, col)
                    self.print_board()
                    if self.check_winner():
                        print(f"{self.current_player} hat gewonnen!")
                        break
                    else:
                        self.current_player = 'Player 2' if self.current_player == 'Player 1' else 'Player 1'
                    if self.is_board_full():
                        print("Das Spiel endet unentschieden.")
                        break
                else:
                    print("Ungültige Eingabe. Bitte Zeile und Spalte zwischen 1 und 3 wählen.")
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie ganze Zahlen ein.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()