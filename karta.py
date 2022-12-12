class Board:
    def __init__(self, size):
        # Initialize the size of the board
        self.size = size
        # Initialize the board with empty cells
        self.cells = [['O' for i in range(self.size)]
                      for j in range(self.size)]
        self.coord_x = 0
        self.coord_y = 0

    def __str__(self):
        # This method is called when the object is printed,
        # e.g. print(my_board)
        # Create a string representation of the board
        board_str = ''
        for row in self.cells:
            # Add each cell and a space to the string
            board_str += ' '.join(row) + '\n'
        # Return the string
        return board_str

    def set_cell(self, row, col, value):
        # Set the value of the cell at the given row and column
        self.cells[row][col] = value

    def size_board(self):
        size = input("Choose your size of the map, 4, 5 or 8\n")
        if size == "4":
            self.my_board = Board(4)
            print(self.my_board)
        elif size == "5":
            self.my_board = Board(5)
            print(self.my_board)
        elif size == "8":
            self.my_board = Board(8)
            print(self.my_board)
        else:
            print("Try again!")

    def starting_pos(self):
        pos = input("""Wich corner would you like to start?
                1. Left uppercorner
                2. Right uppercorner
                3. Left bottom corner
                4. Right bottom corner\n""")
        if pos == "1":
            self.my_board.set_cell(0, 0, "H")
            print(self.my_board)
        elif pos == "2":
            self.my_board.set_cell(0, self.size - 1, "H")
            print(self.my_board)
        elif pos == "3":
            self.my_board.set_cell(self.size - 1, 0, "H")
            print(self.my_board)
        elif pos == "4":
            self.my_board.set_cell(self.size - 1, self.size - 1, "H")
            print(self.my_board)
        else:
            print("Try again!")

    def vart_är_jag(self):
        for j in self.my_board.cells:
            for i in j:
                if i == 'H':
                    self.coord_x = self.my_board.cells.index(j)
                    self.coord_y = j.index(i)

    def moving_topos(self):
        while True:
            self.vart_är_jag()
            move = input("""\n
                Enter Direction:
                1. Left
                2. Right
                3. Up
                4. Down \n""")
            try:
                if move == "1":
                    self.my_board.set_cell((self.coord_x), self.coord_y, "X")
                    self.my_board.set_cell(
                        self.coord_x, (self.coord_y - 1), 'H')
                    print(self.my_board)
                elif move == "2":
                    self.my_board.set_cell((self.coord_x), self.coord_y, "X")
                    self.my_board.set_cell(
                        self.coord_x, (self.coord_y + 1), 'H')
                    print(self.my_board)
                elif move == "3":
                    self.my_board.set_cell((self.coord_x), self.coord_y, "X")
                    self.my_board.set_cell(
                        (self.coord_x - 1), self.coord_y, 'H')
                    print(self.my_board)
                elif move == "4":
                    self.my_board.set_cell((self.coord_x), self.coord_y, "X")
                    self.my_board.set_cell(
                        (self.coord_x + 1), self.coord_y, 'H')
                    print(self.my_board)
            except IndexError:
                print("You can't go outside the map!")


def main():
    b = Board(0)
    b.size_board()
    b.starting_pos()
    b.moving_topos()


if __name__ == '__main__':
    main()