class Cell:
    def __init__(self, cell):
        self.cells_in_cell = cell
        self.sm = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cells_in_cell}')

    def __sub__(self, other):
        if self.cells_in_cell - other.cells_in_cell >= 0:
            return Cell(abs(self.cells_in_cell - other.cells_in_cell))
        else:
            return "Разность количестве клеток меньше нуля"

    def __mul__(self, other):
        return Cell(self.cells_in_cell * other.cells_in_cell)

    def __truediv__(self, other):
        return Cell(self.cells_in_cell // other.cells_in_cell)

    def __add__(self, other):
        return Cell(abs(self.cells_in_cell + other.cells_in_cell))

    def make_order(self, count):
        zt = self.cells_in_cell
        while zt > 0:
            for k in range(1, count + 1):
                print(self.sm, end='')
                zt -= 1
                if zt <= 0:
                    break
            print('\n', end='')


a = Cell(7)
b = Cell(9)
c = Cell(3)
d = Cell(2)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(5)
b.make_order(4)
