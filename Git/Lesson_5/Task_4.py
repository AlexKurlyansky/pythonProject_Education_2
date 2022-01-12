dictionary = {'One': 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new = []

with open('File_task_4', 'r', encoding='utf-8') as file_read, open('File_task4_new', 'w', encoding='utf-8') as file_write:
    for line in file_read.readlines():
        text, num = line.rstrip().split(' - ')
        file_write.write(f'{dictionary[text]} - {num}\n')


