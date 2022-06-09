with open('File_task_5', 'w', encoding='utf-8') as file_write:
    numb = input('Введите числа через пробел: ')
    print(numb, file=file_write)

with open('File_task_5') as file:
    content = file.read().rstrip().split()
    numb = [int(number) for number in content if number .isdigit()]
    print(numb)
    print(sum(numb))