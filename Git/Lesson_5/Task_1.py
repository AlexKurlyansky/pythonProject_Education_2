with open('File_1', 'w', encoding='utf-8') as file:
    text = input('Введите текст: ')
    while text:
        file.write(text+'\n')
        text = input('Введите текст: ')
