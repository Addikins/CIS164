def dictionarysearch(chapter_number):
    chapters = {"Python Basics": "1", "Flow Control": "2", "Functions": "3", "Lists": "4", "Dictionaries and Structuring Data": "5"}
    if chapter_number == 0:
        for chapter_name, chapter_num in chapters.items():
            print("Chapter " + chapter_num + ": ", chapter_name)
    else:
        for chapter_name, chapter_num in chapters.items():
            if str(chapter_number) == chapter_num:
                print("Chapter " + chapter_num + ": " + chapter_name)


def check_for_chapter(chapter_number):
    if 5 >= chapter_number >= 0:
        dictionarysearch(chapter_number)
    else:
        print("That is not a invalid chapter number.")


def get_chapter(chapter_number):
    if chapter_number == 0:
        all_chapters = {}
        for x in range(1, 6):
            all_chapters += dictionarysearch(x)
        print(all_chapters)
    else:
        print(dictionarysearch(chapter_number))


user_selection = int(input("Please enter a chapter number or enter '0' to display all chapters: "))
check_for_chapter(user_selection)

