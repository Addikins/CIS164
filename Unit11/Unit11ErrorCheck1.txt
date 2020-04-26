def get_golfers():
    global name
    golfer_number = 0
    while name != "":
        while True:
            try:
                score = int(input("Enter Golf Score for " + name + ": "))
                break
            except ValueError:
                print("Score must be a number!")
        golfers["golfer" + str(golfer_number)] = {"name": name, "score": score}
        golfer_number += 1
        name = input("Enter another golfer, or press 'Enter' to end.\n")


def write_to_file():
    golf_file = open("golf.txt", "a+")
    for golfer_number, golfer_items in golfers.items():
        for key in golfer_items:
            golf_file.write(str(golfer_items[key]) + "\n")
    golf_file.close()


golfers = {

}

# For this example I will be entering my pets names as data.
name = input("Enter a Golfer Name: ")
get_golfers()
write_to_file()
