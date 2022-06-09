dictionary = {}
with open('File_task_6', 'r', encoding='utf-8') as file:
    for line in file:
        lesson, *hours = line.split()
        hours_all = [int(hour.rstrip('(л)(пр)(лаб)')) for hour in hours if hour != '-']
        dictionary.update({lesson.rstrip(":"): sum(hours_all)})
print(dictionary)

