src = not False and True or False and not True

# TODO расписать упрощение выражения

result = True and True or False and False # избавляемся от отрицаний
result = True or False # избавляемся от логического "И"
result = True # избавляемся от логического "ИЛИ"

print(src == result)
