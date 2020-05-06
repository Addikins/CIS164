# Intended for single names, not full names.
# To sort with full names, I most likely would have used a dictionary.


def get_name():
    while True:
        try:
            name_entry = str(input("Enter a unique name or STOP to finish entering names: "))
            break
        except ValueError:
            print("That's not a real name!")
    return name_entry


def setup_list():
    print("Enter some names and I'll hold onto them and sort them for you.")
    entered_name = get_name()
    while entered_name.lower() != "stop":
        names_list.append(entered_name)
        entered_name = get_name()


def display_names():
    for name in names_list:
        print(name)


names_list = list()
setup_list()
print("\n\nHere are the names you entered:")
display_names()

print("\nIf we order them alphabetically they'll look like this:")
names_list.sort()
display_names()

print("\nIf we order them in reverse alphabetical order they'll display as so:")
names_list.sort(reverse=True)
display_names()

print("\nAs a BONUS, here are the names ordered by length (Ascending):")
names_list.sort(key=len)
display_names()
