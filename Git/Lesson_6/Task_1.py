from itertools import cycle
from time import sleep

class Light:
    colors = ("Красный", "Жёлтый", "Зеленый")
    time_work = (7, 2, 10)
    lights = ["Красный", "Желтый", "Зеленый"]

    def __init__(self, color):
        self.__color = color

    def working(self):
        my_cycle = cycle(self.colors)
        for lighting in my_cycle:
            if self.__color == lighting:
                print(self.lights[self.colors.index(self.__color)])
                sleep(self.time_work[self.colors.index(self.__color)])
                self.__color = next(my_cycle)

my_light = Light("Красный")
my_light.working()