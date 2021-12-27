
""" Ай-яй-яй, читерство
text = input("Введите фразу: ")
print(text.title())

"""

def int_func(word):
    return word.capitalize()

inp_text = input('Введите любую фразу: ')
result_list = []
inp_words = inp_text.split()
for i in inp_words:
    result_list.append(int_func(i))
print(" ".join(result_list))

