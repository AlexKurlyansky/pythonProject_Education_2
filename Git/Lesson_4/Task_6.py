from itertools import count, cycle

for i in count(int(input('Введите начальное число до 1000: '))):
    if i == 1001:
        break
    print(i)

def my_gen():
    num = int(input('Введите число: '))
    for i in count(num):
        if i > num+100:
            break
        yield i
for i in my_gen():
    print(i)


my_list = "ABCDEFG"
numb_cycle = 0
for el in cycle(my_list):
    if el == my_list[0]:
        numb_cycle += 1
    if numb_cycle < 3:
        print(el)
    else:
        break