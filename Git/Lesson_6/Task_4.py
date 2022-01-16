class Cars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль марки {self.name}, цвета {self.color} двигается со скоростью {self.speed}")

    def stop(self):
        print(f"Автомобиль {self.color} цвета, марки {self.name} остановился")

    def turn(self, direction):
        print(f"Автомобиль {self.color} цвета, марки {self.name} повернул {direction}")

    def show_speed(self):
        print(f"Автомобиль двигается со скоростью {self.speed}")

class TownCar(Cars):
    def show_speed(self):
        if self.speed > 60:
            print("Потише бричку, вы в городе!")
        else:
            Cars.show_speed(self)

class SportCar(Cars):
    def __init__(self, speed, color, name):
        Cars.__init__(self, speed, color, name, is_police=False)
        print(f"Спортивный автомобиль {self.name} проходит квалификационный раунд")

class WorkCar(Cars):
    def show_speed(self):
        if self.speed > 60:
            print("Потише бричку, вы в городе!")
        else:
            Cars.show_speed(self)

class PoliceCar(Cars):
    def __init__(self, speed, color, name):
        Cars.__init__(self, speed, color, name, is_police=True)
        print(f"Полицейский автомобиль {self.name} производит патрулирование района")

my_town_car = TownCar(85, "Серебро", "BMW", False)
my_town_car.go()
my_town_car.turn('Направо')
my_town_car.stop()
my_town_car.show_speed()

my_sport_car = SportCar(185, "Красного", "BMW M3")
my_sport_car.go()
my_sport_car.turn('Налево')
my_sport_car.stop()
my_sport_car.show_speed()

my_work_car = WorkCar(65, "Жёлтого", "Ford Transit", False)
my_work_car.go()
my_work_car.turn('Налево')
my_work_car.stop()
my_work_car.show_speed()

my_police_car = PoliceCar(80, "Спец-окрас", "Volkswagen Passat")
my_police_car.go()
my_police_car.turn('Направо')
my_police_car.stop()
my_police_car.show_speed()