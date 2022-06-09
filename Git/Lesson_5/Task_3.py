sum = 0

with open('File_task_3', 'r', encoding='utf-8') as file:
    content = file.readlines()
    print(content)
    for line in content:
        surname, cash = line.split()
        sum += int(cash)
        if int(cash) < 20000:
            print(f'У данных сотрудников оклад менее 20000 рублей: {surname} и составляет  {cash} рублей')

print(f'Средний оклад по всем сотрудникам составляет: {int(sum/len(content))} рублей')



