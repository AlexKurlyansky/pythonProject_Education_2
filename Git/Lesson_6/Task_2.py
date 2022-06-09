class Road:
    def __init__(self, width, lenght):
        self._width = width
        self._lenght = lenght

    @property
    def square(self):
       return self._lenght * self._width

    def weight_asphalt(self, weight, thickness):
        asphalt = self.square * weight * thickness
        return asphalt

my_road = Road(20, 5000)
print(my_road.weight_asphalt(25, 1))