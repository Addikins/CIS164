school = "cochise college"
place = "online"


def slice5(first_string, second_string):
    return first_string[0:5], second_string[0:5]


print("First five characters of School and Place strings: ")
print(slice5(school, place))


def get_first_char(first_string, second_string):
    return first_string[0], second_string[0]


print("\nFirst character of School and Place strings: ")
print(get_first_char(school, place))


def get_last_char(first_string, second_string):
    return first_string[-1], second_string[-1]


print("\nLast character of School and Place strings: ")
print(get_last_char(school, place))


def to_title(first_string, second_string):
    if not first_string.istitle() and not second_string.istitle():
        return first_string.title(), second_string.title()
    else:
        return first_string, second_string


print("\nSchool and Place strings in Title Form: ")
print(to_title(school, place))


def check_enrollment(first_string, second_string):
    if "cochise" in first_string.lower() and "online" in second_string.lower():
        return "Great, you go to Cochise College Online!"
    else:
        return "You're not enrolled online. You should check out Cochise College Online!"


print("\n\nChecking to see if you go to Cochise College Online...\n\n\n" + check_enrollment(school, place))
