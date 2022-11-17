from random import randint

def get_unique_list_numbers(lenghth_of_list = 15, min_num = -10, max_num = 10) -> list[int]:

    list_ = []
    while len(list_) < lenghth_of_list:
        num = randint(min_num, max_num)
        if list_.count(num) == 0:
            list_.append(num)

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
