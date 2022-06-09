with open('File_1') as file:
    content = file.readlines()
    print('Количество строк в файле: ', len(content))
    for text, words in enumerate(content):
        print(f'Количество слов в строке: ', len(words.split()))
