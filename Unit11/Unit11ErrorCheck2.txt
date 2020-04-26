import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def get_golfers():
    global name
    golfer_number = 0
    while name != "":
        logging.debug("Beginning of loop " + str(golfer_number + 1) + " of the 'get_golfers' function.")
        while True:
            try:
                score = int(input("Enter Golf Score for " + name + ": "))
                break
            except ValueError:
                print("Score must be a number!")
        golfers["golfer" + str(golfer_number)] = {"name": name, "score": score}
        golfers["golfer" + str(golfer_number)] = {"name": name, "score": score}
        golfer_number += 1
        name = input("Enter another golfer, or press 'Enter' to end.\n")


def write_to_file():
    golf_file = open("golf.txt", "a+")
    for golfer_number, golfer_items in golfers.items():
        for key in golfer_items:
            golf_file.write(str(golfer_items[key]) + "\n")
    golf_file.close()


logging.debug("Start of program. Initialize golfers dictionary.")
golfers = {

}

# For this example I will be entering my pets names as data.
name = input("Enter a Golfer Name: ")
logging.debug("Call first function, gets input from user.")
get_golfers()
logging.debug("Call second function, writes dictionary of golfers and the information to text file.")
write_to_file()
logging.debug("End of program.")

