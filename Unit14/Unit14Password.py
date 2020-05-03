import re


def check_for_digits(pw):
    digit_regex = re.compile(r'\d')
    match = digit_regex.findall(pw)
    if len(match) >= 3:
        return ''
    else:
        return 'Password does not contain at least three digits.'


def check_for_lowercase(pw):
    upper_regex = re.compile(r'[a-z]')
    match = upper_regex.findall(pw)
    if len(match) >= 3:
        return ''
    else:
        return 'Password does not contain at least three lowercase letters.'


def check_for_uppercase(pw):
    upper_regex = re.compile(r'[A-Z]')
    match = upper_regex.findall(pw)
    if len(match) >= 3:
        return ''
    else:
        return 'Password does not contain at least three uppercase letters.'


def check_for_special_characters(pw):
    upper_regex = re.compile(r'[!#$%&()*+,./:;<=>?\\@\-^_`\[\]{|}~]')
    match = upper_regex.findall(pw)
    if len(match) >= 3:
        return ''
    else:
        return 'Password does not contain at least three special characters.'


def check_for_length(pw):
    if 12 <= len(pw) <= 24:
        return ''
    elif len(pw) < 12:
        return 'Password is too short, it must be at least 12 characters long.'
    else:
        return 'Password is too long, it must be no more than 24 characters long.'


def valid_password():
    is_valid = False
    while not is_valid:
        password = input("Please Enter a Password: ")
        password_functions = {check_for_digits(password), check_for_lowercase(password),
                              check_for_uppercase(password), check_for_special_characters(password), check_for_length(password)}
        is_valid = True
        for item in password_functions:
            if item != '':
                print(item)
                is_valid = False
    print("The password entered meets all requirements!")


valid_password()
