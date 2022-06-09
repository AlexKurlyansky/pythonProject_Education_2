class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    @property
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    @property
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

my_position = Position('Пётр', 'Петров', 'водитель', 60000, 15000)
print(f"Полная заработная плата с учетом премии у сотрудника {my_position.get_full_name} составляет: {my_position.get_total_income}")

