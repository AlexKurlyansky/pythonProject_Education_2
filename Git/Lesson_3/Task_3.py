def my_func():
    x = int(input('Введите х: '))
    y = int(input('Введите y: '))
    z = int(input('Введите z: '))

    if (x >= y or x >= z) and (y >= z or y >= x):
        summ = x + y
    elif (x >= y or x >= z) and (z >= y or z >= x):
        summ = x + z
    else:
        summ = y + z
    return summ
result = my_func()
print(result)

def my_func(x, y, z):
    my_list = [x, y, z]
    my_list.sort()
    return sum(my_list[1:3])
print(my_func(30, 10, 50))