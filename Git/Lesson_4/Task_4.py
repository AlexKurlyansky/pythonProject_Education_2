from random import randint

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(my_list)
my_list_2 = [el for el in my_list if my_list.count(el) == 1]
print(my_list_2)

random_list = [randint(0, 20) for i in range(20)]
print(f'Список {random_list}')
print({i for i in random_list if random_list.count(i) == 1})