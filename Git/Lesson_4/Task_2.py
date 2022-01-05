# #
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list_2 = [i for num, i in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_list_2}')

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list_2 = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_list_2}')


def my_gen():
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print(f'Исходный список:  {my_list}')

    my_list_2 = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
    print(f'Обновленный список:  {my_list_2}')
if __name__ == "__main__":
    my_gen()
