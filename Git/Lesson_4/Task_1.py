
# from sys import argv
#
# script_name, time, bet_hour, bonus = argv
# print("Имя скрипта: ", script_name)
# print("Время работы: ", time)
# print("Ставка в час: ", bet_hour)
# print("Премия: ", bonus)
# print("Итоговая выплата: ", int(time) * int(bet_hour) + int(bonus))
#

def wages():
    try:
        time = int(input('Выработка в часах: '))
        bet_hour = int(input('Ставка в час: '))
        bonus = int(input('Премия: '))
        summ = time * bet_hour + bonus
        print(f'Заработная плата сотрудника составляет: {summ} рублей')
    except ValueError:
        return print('Введены некорректные данные!')
wages()