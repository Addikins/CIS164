import webbrowser, threading


def openWebsite():
    webbrowser.open("https://xkcd.com/210/")
    webbrowser.open("http://xkcd.com/1303/")
    webbrowser.open("https://xkcd.com/1309/")
    webbrowser.open("https://xkcd.com/1349/")
    webbrowser.open("https://xkcd.com/1373/")
    webbrowser.open("https://xkcd.com/1742/")
    webbrowser.open("https://www.cochise.edu/")


website_thread = threading.Thread(target=openWebsite)
website_thread.start()
