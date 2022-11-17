from random import sample

def get_random_password(lenght_of_password = 8) -> str:

    list_ = sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', lenght_of_password)

    return ''.join(list_)

print(get_random_password())

