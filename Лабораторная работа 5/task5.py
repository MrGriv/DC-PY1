import random

def get_random_password() -> str:
    lenght_of_password = 8
    password = ''
    list_ = random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', lenght_of_password)
    for i in range(lenght_of_password):
        password += str(list_[i])
    return password

print(get_random_password())

