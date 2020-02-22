import re

def is_username_valid(input_string):
    regex = re.compile('^[^_][a-z_]{5,8}$', re.I)
    match = regex.match(str(input_string))
    return print(bool(match))

def is_password_valid(input_string):
    regex = re.compile('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[\d])(?=.*?[!]).{9}$', re.I)
    match = regex.match(str(input_string))
    return print(bool(match))

user_inpt = input("Masukkan username : ")
is_username_valid(user_inpt)
pass_inpt = input("Masukkan password : ")
is_password_valid(pass_inpt)
