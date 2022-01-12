import json
list = []
dict_profit = {}
dict_loss = {}

with open('File_task_7', 'r', encoding='utf-8') as file:
    profit_list = []
    for line in file.readlines():
        company, _, income, loss = line.rstrip().split()
        profit = int(income) - int(loss)
        if profit > 0:
            profit_list.append(profit)
            dict_profit.update({company: profit})
        else:
            dict_loss.update({company: profit})
list.append(dict_profit)
list.append(dict_loss)
list.append({"Average profit:": sum(profit_list)/len(profit_list)})

with open("File_task7.json", "w", encoding="utf-8") as file:
    json.dump(list, file)




