
class Error_Val:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Введите числа и нажимайте Enter: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Вы ввели не число!")
                next = input(f'Попробовать еще раз? Y/N ')

                if next == 'Y' or next == 'y':
                    print(check.my_input())
                elif next == 'N' or next == 'n':
                    return f'До свидания! Текущий список: {self.my_list}'
                else:
                    return f'Аварийная остановка, вы пьяны! Текущий список: {self.my_list}'

check = Error_Val(1)
print(check.my_input())

