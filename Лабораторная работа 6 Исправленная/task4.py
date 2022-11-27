import json

INPUT_FILE = "input_1.csv"




def csv_to_list_dict(csv_file, delimiter = ',', new_line = '\n') -> list[dict]:

    list_ = []
    list_dict = []
    with open(csv_file) as f:
        for item in f:
            item = item.rstrip(new_line)
            list_.append(item.split(delimiter))

    headers_list = list_.pop(0)

    for item in list_:
        dict_ = dict(zip(headers_list, item))
        list_dict.append(dict_)

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

