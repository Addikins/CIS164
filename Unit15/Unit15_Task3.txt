import secrets
import string
import re


def check_password(pw):
    # Checks that there is at least one uppercase, lowercase,
    # number and special character in the password.
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    number_regex = re.compile(r'[0-9]')
    symbol_regex = re.compile(r'[!#$%&()*+,./:;<=>?\\@\-^_`\[\]{|}~]')

    if uppercase_regex.search(pw) is not None and lowercase_regex.search(pw) is not None and number_regex.search(pw) is not None and symbol_regex.search(pw) is not None:
        return True
    else:
        return False


def get_password_length():
    while True:
        try:
            pass_length = int(input("Enter the desired password length (minimum length of 4)\n"))
            if pass_length >= 4:
                break
        except ValueError:
            print("Not a valid password length!")
    return pass_length


def generate_password(password_length):
    password = ""
    while check_password(password) is not True:
        password = ""
        for character in range(0, password_length):
            password_building_blocks = [secrets.randbelow(10),
                                        secrets.choice(string.ascii_letters),
                                        secrets.choice(symbols)]
            password += str(secrets.choice(password_building_blocks))
    return password


symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',',
           '.', '/', '\\', ':', ';', '<', '=', '>', '?', '@',
           '-', '^', '_', '`', '[', ']', '{', '|', '}', '~']


print("Your password is: ", generate_password(get_password_length()))
