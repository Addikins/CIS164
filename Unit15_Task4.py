
def get_selection():
    selection = 0
    while 0 >= selection or selection >= 5:
        print("          1. Calculator\n"
              "          2. Text Editor\n"
              "          3. Web Browser\n"
              "          4. Quit Menu")
        try:
            selection = int(input())
        except ValueError:
            print("Not a valid selection. Please choose an option: ")
    return selection


print("\n   ------Python Task Menu------   \n")
get_selection()

