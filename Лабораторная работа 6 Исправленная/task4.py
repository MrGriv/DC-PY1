import json

INPUT_FILE = "input_1.csv"




def csv_to_list_dict(csv_file, delimiter = ',', new_line = '\n') -> list[dict]:

    list_dict = []

    with open(csv_file) as f:
        headers_list = f.readline().rstrip(new_line).split(delimiter)
        for item in f:
            item = item.rstrip(new_line).split(delimiter)
            list_dict.append(dict(zip(headers_list, item)))

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

