class StoreMashines:

    def __init__(self, tech_type, name, price, quantity, *args):
        self.tech_type = tech_type
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_unit = {'Тип устройства': self.tech_type, 'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}
    my_store_full = []
    my_store = []
    def __str__(self):
        return f'{self.tech_type}{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:

            type_tech = input("Введите тип устройства: ")
            unit = input('Введите наименование: ')
            unit_p = int(input('Введите цену за ед: '))
            unit_q = int(input('Введите количество: '))
            unique = {'Тип устройства': type_tech, 'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def __init__(self, tech_type, name, price, quantity, colors):
        super().__init__(tech_type, name, price, quantity, colors)
        self.colors = colors

class Scanner(StoreMashines):
    def __init__(self, tech_type, name, price, quantity):
        super().__init__(tech_type, name, price, quantity)

class Xerox(StoreMashines):
    def __init__(self, tech_type, name, price, quantity):
        super().__init__(tech_type, name, price, quantity)

class Notebook(StoreMashines):
    def __init__(self, tech_type, name, price, quantity, ram, system_type):
        super().__init__(tech_type, name, price, quantity)
        self.ram = ram
        self.system_type = system_type


unit_1 = Printer('Принтер', 'hp', 2000, 5, '[black]')
unit_2 = Scanner('Сканер', 'Canon', 1200, 5)
unit_3 = Xerox('Ксерокс', 'Xerox', 1500, 1)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
