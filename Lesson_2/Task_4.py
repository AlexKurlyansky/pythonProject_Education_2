
text = input('Введите какую-нибудь фразу: ')
text_2 = text.split()
#number = 1
# for i in text_2:
#     print(number, i[:10])
#     number += 1

for index, word in enumerate(text_2, 1):
    print(index, word[:10])



