def indexvalue(index):
    locations = "Benson", "Douglas", "Sierra Vista", "Online"
    try:
        return locations[index]
    except IndexError:
        print('There is no index value for that number within the list')
