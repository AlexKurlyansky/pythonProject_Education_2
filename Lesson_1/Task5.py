proceeds = int(input('Напишите выручку Вашей компании за год: '))
costs = int(input('Напишите Ваши издержки за год: '))
employees = int(input('Напишите количество Ваших сотрудников: '))
profit = ()
profit_emp = ()
lesion = ()
if proceeds > costs:
    profit = proceeds - costs
    print('Ваш профит за этот год составил: ', profit)
    profit_emp = profit/employees
    print('Доход на каждого сотрудника составляет:', profit_emp)
else:
    lesion = proceeds - costs
    print('Ваша компания находится в убытке: ', lesion, 'Примите меры!')
