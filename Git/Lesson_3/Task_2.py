names = input('Введите Ваше имя: ')
surnames = input('Введите Вашу фамилию: ')
year_of_birth = input('Введите Ваш год рождения: ')
cities = input('Введите Ваш город: ')
emailes = input('Введите Вашу электронную почту: ')
phones = input('Введите Ваш номер телефона: ')

def users():
    return ' '.join([names, surnames, year_of_birth, cities, emailes, phones])
print(f'{names} {surnames} {year_of_birth} года рождения, проживаете в городе {cities}, Ваша электронная почта:'
      f'{emailes}, номер телефона: {phones}')


def users(name, surname, birth, city, email, phone):
    return ' '.join([name, surname, birth, city, email, phone])
print(users(name="Alex", surname="Kurlyansky", birth="19.03.84", city="Krasnodar", email="gde-to@tochka.com",
            phone="322-223"))