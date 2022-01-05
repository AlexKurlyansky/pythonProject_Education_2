from functools import reduce


def my_func(el, el_s):
    return el * el_s

print({el for el in range(100, 1001) if el % 2 == 0})
print({reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])})

my_list = [el for el in range(100, 1001, 2)]
print(my_list)
result = reduce(lambda x, y: x*y, my_list)
print(result)
