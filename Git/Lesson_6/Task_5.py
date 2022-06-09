class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки:")

class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f"Мы рисуем с помощью {self.title}")

class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f"Мы рисуем с помощью {self.title}")

class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f"Мы рисуем с помощью {self.title}")

pen = Pen("Ручки")
pencil = Pencil("Карандаша")
handle = Handle("Маркера")
pen.draw()
pencil.draw()
handle.draw()