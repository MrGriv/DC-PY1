list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_num = list_numbers[0]
index_max_num = 0

for index, current_num in enumerate(list_numbers):  # проверка на максимальный элемент и запись его индекса в списке
    if max_num < current_num:
        max_num = current_num
        index_max_num = index

list_numbers[index_max_num], list_numbers[-1] = list_numbers[-1], max_num  # замена позиций найденного
# первого максимального и последнего элемента
print(list_numbers)
