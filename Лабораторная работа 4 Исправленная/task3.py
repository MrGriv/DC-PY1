def delete(list_, index=None):
    if index is None or index == -1:
        return list_[:-1]  # возврат нового списка без последнего элемента
    else:
        return list_[:index] + list_[index+1:]  # разделение списка на список до удаляемого элемента и на список после
    # удаляемого элемента. Далее списки суммируются


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

print(delete([0, 1, 1, 2, 3], index=-1))  # Проверка по просьбе преподавателя
