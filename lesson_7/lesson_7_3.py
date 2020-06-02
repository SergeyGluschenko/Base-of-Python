class Cell:
    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __add__(self, other):
        print(self.count_cell + other)

    def __sub__(self, other):
        if self.count_cell - other > 0:
            print(self.count_cell - other)
        else:
            print('Организм вымер как динозавр(')

    def __mul__(self, other):
        print(self.count_cell * other)

    def __truediv__(self, other):
        print(int(self.count_cell / other))

    def make_order(self, piece_in__line):
        if self.count_cell // piece_in__line != 0:
            for i in range(self.count_cell // piece_in__line):
                print(piece_in__line * '*')
        if self.count_cell % piece_in__line != 0:
            print((self.count_cell % piece_in__line) * '*')


cell_param = Cell(56)


cell_param + 87
cell_param * 2
cell_param / 3
cell_param - 16
cell_param.make_order(11)