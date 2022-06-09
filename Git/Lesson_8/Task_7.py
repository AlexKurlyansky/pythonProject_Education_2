class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b}j'


z_1 = ComplexNumber(9, 5)
z_2 = ComplexNumber(-5, 6)
print(f"Сумма равна: {z_1 + z_2}")
print(f"Умножение равно: {z_1 * z_2}")
z1 = complex(9, 5)
z2 = complex(-5, 6)
print(f"Сумма равна: {z1 + z2}")
print(f"Умножение равно: {z1 * z2}")
