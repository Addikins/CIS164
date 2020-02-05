lineSpacing = "\n" * 5
while True:
    print("Hello. Please enter your name.")
    name = input("NAME: ")

    if name != "Bob":
        print("Your name is not Bob, go away!", lineSpacing)
    elif name == "Bob":
        print("Please input your password Bob.")
        password = input("PASSWORD: ")
        while password != "pass123":
            print("You have entered the wrong password, go away!")
            password = input("PASSWORD: ")
        print("User Bob, your access has been granted, enjoy your day!")
        break
