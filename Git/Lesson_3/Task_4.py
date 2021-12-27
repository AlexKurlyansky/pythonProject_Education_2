def my_func(x, y):
    PhD = x**y

    return PhD
result = my_func(5, -4)
print(result)

def my_func(x: int, y: int) -> float:
    if y > 0:
        return
    elif y == 0:
        return 1
    elif x <= 0:
        return
    else:
        PhD = 1
        while y < 0:
            PhD *= 1/x
            y += 1
        return PhD
result = my_func(5, -4)
print(result if result else "Некорректные данные!")