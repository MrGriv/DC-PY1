import json

INPUT_FILE = "input_1.csv"




def csv_to_list_dict(csv_file, delimiter = ',', new_line = '\n') -> list[dict]:

    list_ = []
    list_dict = []
    with open(csv_file) as f:
        for item in f:
            list_.append(item.split(f'{delimiter}'))
    for last_elem in list_:
        last_elem[-1] = last_elem[-1].rstrip(f'{new_line}')

    headers_list = list_.pop(0)

    for item in list_:
        dict_ = {}
        count = 0
        for elem in item:
            dict_.update({headers_list[count]: elem})
            count += 1
        list_dict.append(dict_)
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

