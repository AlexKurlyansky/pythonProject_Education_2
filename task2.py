value = int(input("Введите число: "))
while value > 10 or value <= 0:
    print("Введите число от 1 до 10")
    value = int(input("Введите число: "))
else:
    print("Ваше число во второй степени =", value ** 2)
