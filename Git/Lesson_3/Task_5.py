
def summ(input_number):
    number = input_number.split()
    my_sum = 0
    for i in number:
        if i:
            try:
                if i == 'q' or i == 'Q':
                    return my_sum, False
                else:
                    my_sum += int(i)
            except ValueError:
                continue
    return my_sum, True
continue_flag = True
result_sum = 0
while continue_flag:
    number = input('Введите числа через пробел, либо нажмите Q для выхода: ')
    current_sum, continue_flag = summ(number)
    result_sum += current_sum
    print('Промежуточная сумма: ', result_sum)
print('Общая сумма: ', result_sum)
