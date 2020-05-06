import os
import datetime


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


options = {
    "1": "gnome-calculator",
    "2": "gedit",
    "3": "firefox",
    "4": "exit"
}
while True:
    current_datetime = datetime.datetime.now()
    print("\n   ------Python Task Menu------   \n",
          current_datetime.strftime("   %b %d, %Y"),
          current_datetime.strftime("       %H:%M:%S\n"))
    command = options[str(get_selection())]
    if command == "exit":
        break
    os.system(command)
