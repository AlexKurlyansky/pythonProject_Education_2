class Data:
    def __init__(self, data_mounth_year):
        self.data_mouth_year = data_mounth_year

    @classmethod
    def input_data(cls, data_mounth_year):
        my_data = []
        for i in data_mounth_year.split(' '):
            if i != ' ': my_data.append(i)
        return int(my_data[0]), int(my_data[1]), int(my_data[2])

    @staticmethod
    def static_metod(data, mounth, year):
        if 1 <= data <= 31:
            if 1 <= mounth <=12:
                if 0 <= year <= 2022:
                    return f'Статический вывод: {data} {mounth} {year}'
                else:
                    print("Это либо будущее, либо далекое прошлое")
            else:
                print("Введен некорректный месяц")
        else:
            print("Введен некорректный день")

    def __str__(self):
        return f'Введеная дата: {Data.input_data(self.data_mouth_year)}'

input_day = Data(input('Введите дату через пробел: '))
print(input_day)
print(Data.input_data('14 03 1984'))
print(input_day.input_data('09 08 1984'))
print(Data.static_metod(13, 3, 1984))
print(Data.static_metod(13, 3, -1984), f'13, 3, -1984')
print(Data.static_metod(13, 3, 11984), f'13, 3, 11984')
print(Data.static_metod(13, 13, 1984), f'13, 13, 1984')
print(Data.static_metod(133, 3, 1984), f'133, 3, 1984')

