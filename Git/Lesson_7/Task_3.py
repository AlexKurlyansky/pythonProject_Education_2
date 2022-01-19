class Cell:

    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            print('Результат отрицательный')

    def __mul__(self, other):
       return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.number // param) + '*' * (self.number % param)

cells_1 = Cell(35)
cells_2 = Cell(15)
print(cells_1.make_order(4))
print(cells_2.make_order(5))
print()
cells_3 = cells_1 + cells_2
print(f"Сложение: \n{cells_3.make_order(8)}")
cells_4 = cells_1 - cells_2
print(f"Вычитание: \n{cells_4.make_order(3)}")
# cells_5 = cells_2 - cells_1
# print(cells_5.make_order(2))
cells_6 = cells_1 * cells_2
print(f"Умножение: \n{cells_6.make_order(15)}")
cells_7 = cells_1 / cells_2
print(f"Деление: \n{cells_7.make_order(8)}")


