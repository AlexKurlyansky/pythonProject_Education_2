second = int(input('Введите число в секундах: '))
hours = int(second // 3600)
minuts = int((second % 3600) // 60)
minuts_cel = int(second % 60)

print(second, 'секунд - это: ', 'чч:', hours, 'мм:', minuts, 'сс:', minuts_cel)
