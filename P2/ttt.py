"""Tom Schäfer, Erik Gladitz FPP WS23/24 - Mo56x_Gruppe_03"""


class Player:
    def __init__(self, symbol='X'):
        self.symbol = symbol

class Board:
    """ create gamespace & allow printing, making moves & check filledness """
    def __init__(self):
        # list comprehension: construct new list from old one (https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions)
        self.cells = [['—']*3 for _ in range(3)]

    def view(self):
        print('\n'.join([' '.join(row) for row in self.cells]), '\n')

    def strike(self, player, row, col):
        if self.cells[row - 1][col - 1] == '—':
            self.cells[row - 1][col - 1] = player.symbol
            return True
        else:
            print("Field occupied. Try again!\n")
            return False

    def full(self):
        return all(['—' not in row for row in self.cells])

class TicTacToe:
    """ init components & implement win-checking & game logic """
    def __init__(self):
        self.board = Board()
        self.player = Player()

    def win(self):
        for i in range(3):
            if self.board.cells[0][i] == self.board.cells[1][i] == self.board.cells[2][i] != '—' or \
                self.board.cells[i][0] == self.board.cells[i][1] == self.board.cells[i][2] != '—':
                return True

        if self.board.cells[0][0] == self.board.cells[1][1] == self.board.cells[2][2] != '—' or \
            self.board.cells[0][2] == self.board.cells[1][1] == self.board.cells[2][0] != '—':
            return True

        return False

    def play(self):
        print("TicTacToe started.\n")
        self.board.view()

        while True:
            print(f"{self.player.symbol}'s turn.")
            try:
                row, col = map(int, input("Enter space-seperated row (1—3) & column (1|3): ").split())
                if 1 <= row <= 3 and 1 <= col <= 3:
                    if self.board.strike(self.player, row, col):
                        self.board.view()
                    else:
                        self.board.view()
                        continue

                    if self.win():
                        print(f"{self.player.symbol} wins!")
                        break
                    elif self.board.full():
                        print("Conclusion: Draw.")
                        break
                    else:
                        self.player.symbol = 'O' if self.player.symbol == 'X' else 'X'
                else:
                    print("Invalid input. Row and column should be between 1 and 3.\n")
                    self.board.view()
            except ValueError:
                print("Invalid input. Please enter two space-separated whole numbers.\n")
                self.board.view()

if __name__ == "__main__":
    TicTacToe().play()