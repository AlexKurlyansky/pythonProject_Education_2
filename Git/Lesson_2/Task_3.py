list_season = ['Лето', 'Осень', 'Зима', 'Весна']
dict_season = { 1 : 'summer', 2 : 'autumn', 3 : 'winter', 4 : 'spring'}
try:
    mounth = int(input('Введите номер месяца, который Вас интересует от 1 до 12: '))
except ValueError:
    print('Введите числа от 1 до 12!')
else:
    if mounth == 1 or mounth == 12 or mounth == 2:
        print(list_season[2])
    elif mounth == 3 or mounth == 4 or mounth == 5:
        print(list_season[3])
    elif mounth == 6 or mounth == 7 or mounth == 8:
        print(list_season[0])
    elif mounth == 9 or mounth == 10 or mounth == 11:
        print(list_season[1])

    else:
        print('Вы неправильно ввели значение, такого месяца не существует')