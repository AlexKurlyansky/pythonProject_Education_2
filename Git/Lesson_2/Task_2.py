number = int(input("Введите количество элементов списка: "))
list_1 = []
x = 0
y = 0
while x < number:
    list_1.append(input("Введите значение списка: "))
    x += 1
print(list_1)
for change in range(int(len(list_1)/2)):
        list_1[y], list_1[y+1] = list_1[y+1], list_1[y]
        y += 2
print(list_1)

