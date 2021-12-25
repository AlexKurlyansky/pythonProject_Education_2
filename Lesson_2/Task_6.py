sum = int(input("Введите количество товара: "))
n = 1

my_list = []
analitics = {}
while n <= sum:
    product = dict({'Название:': input("Введите название товара: "), 'Цена:': input("Введите цену товара: "),
                    'Количество:': input('Введите количество товара: '), 'Ед:': input("Введите единицу измерения: ")})
    my_list.append((len(my_list), product))
    n += 1

print(my_list)

for my_struct in my_list:
    struct_num, struct_into_dict = my_struct
    for key, value in struct_into_dict.items():
        value_list =analitics.get(key, [])
        if value not in value_list:
            value_list.append(value)
        analitics[key] = value_list
for item in analitics.items():
    print(item)
