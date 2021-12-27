def division():
    x = int(input('Введите х: '))
    y = int(input('Введите y: '))
    try:
       div = x / y
    except ZeroDivisionError:
        print('Делить на 0 нельзя!')
    else:
        return div
result = division()
print(result)

def division(x, y):

    try:
       div = x / y
    except ZeroDivisionError:
        print('Делить на 0 нельзя!')
    else:
        return div
result = division(x=4, y=2)
print(result)