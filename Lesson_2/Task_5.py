my_list = [7, 5, 3, 3, 2]
number = int(input('Введите число: '))
""" Да я оказывается злостный Читер)))
my_list.append(number)
print(sorted(my_list, reverse=True))
ну да и ладно...
"""
for index, y in enumerate(my_list):
    if number >= y:
        my_list.insert(index, number)
        break
else:
    my_list.append(number)
print(my_list)
