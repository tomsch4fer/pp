"""Tom Schäfer, Erik Gladitz FPP WS23/24 - Mo56x_Gruppe_03"""


class Player:
    """ creates Player differentiation X/O """
    def __init__(self):
        self.symbol = 'X'

class Board:
    """ creates board to play on & allows printing, checking fullness & making moves """
    def __init__(self):
        self.cells = [['—', '—', '—'],
                      ['—', '—', '—'],
                      ['—', '—', '—']]
        
    def view(self):
        print()
        for row in self.cells:
            print(" ".join(row))
        print()
    
    def strike(self, player, row, col):
        if self.cells[row - 1][col - 1] == '—':
            self.cells[row - 1][col - 1] = 'X' if player.symbol == 'X' else 'O'
            return True
        else:
            print("Field occupied. Try again!")
            return False

    def full(self):
        for row in self.cells:
            if '—' in row:
                return False
        return True
            
class TicTacToe:
    """ initializes game, checks winner & holds game logic """
    def __init__(self):
        self.board = Board()
        self.player = Player()

    def win(self):
        for row in self.board.cells:
            if row[0] == row[1] == row[2] != '—':
                return True

        for col in range(3):
            if self.board.cells[0][col] == self.board.cells[1][col] == self.board.cells[2][col] != '—':
                return True

        if self.board.cells[0][0] == self.board.cells[1][1] == self.board.cells[2][2] != '—':
            return True

        if self.board.cells[0][2] == self.board.cells[1][1] == self.board.cells[2][0] != '—':
            return True

        return False

    def play(self):
        print("TicTacToe started.")
        self.board.view()

        while True:
            print(f"{self.player.symbol}'s turn.")
            try:
                row = int(input("row(|): "))
                col = int(input("column(—): "))
                if 1 <= row <= 3 and 1 <= col <= 3:
                    if self.board.strike(self.player, row, col):
                        self.board.view()
                    else:
                        self.board.view()
                        continue

                    if self.win():
                        print(f"{self.player.symbol} wins!")
                        break
                    else:
                        self.player.symbol = 'O' if self.player.symbol == 'X' else 'X'

                    if self.board.full():
                        print("conclucion: draw.")
                        break
                else:
                    print("Invalid input. row & column are limited from 1 to 3.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()