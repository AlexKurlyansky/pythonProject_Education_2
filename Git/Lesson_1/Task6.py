x = int(input('Результат спортсмена в первый день тренировки: '))
y = int(input('Желаемый результат дистанции: '))
day = 1

while x < y:
    x *= 1.1
    day += 1

print(f'Желаемый результат в {y} км будет достигнут в течении {day} дней')
