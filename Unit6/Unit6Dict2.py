def get_chapter(chapter_num):
    chapters = {"Python Basics": "1", "Flow Control": "2", "Functions": "3", "Lists": "4", "Dictionaries and Structuring Data": "5"}
    for chapterName, chapterNum in chapters.items():
        if chapterNum == chapter_num:
            return chapterName


print("Please choose a chapter number to get the name of a specific chapter.")
selection = input("Enter chapter number: ")


print("You have chosen Chapter " + selection + " in our book, " + get_chapter(selection) + "\n\nhttps://automatetheboringstuff.com/chapter" + selection + "/")

