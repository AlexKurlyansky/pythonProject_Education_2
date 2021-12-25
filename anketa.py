print("Медицинская анкета")
name = input("Введите свое имя: ")
surname = input("Введите свою фамилию: ")
age = int(input("Введите ваш возраст: "))
weight = int(input("Введите Ваш вес: "))
if (age <= 30 and weight < 120) and (age <= 30 and weight > 50):
    print(surname, name, "С Вами все хорошо!")
if (age > 30 and age < 40 and weight < 120) and (age > 30 and weight > 50):
    print(surname, name, "С Вами все хорошо!")
if (age > 30 and age < 40 and weight > 120) or (age > 30 and weight < 50):
     print(surname, name, "Вам нужно заняться собой!")
if (age <= 30 and weight > 120) or (age <= 30 and weight < 50):
     print(surname, name, "Вам нужно заняться собой!")
if (age > 40 and weight > 120) or (age > 40 and weight < 50):
    print(surname, name, "Вам нужно обратиться к врачу!")
if (age > 40 and weight < 120) and (age > 40 and weight > 50):
    print(surname, name, "Вы в порядке!")
