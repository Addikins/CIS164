import webbrowser


websites = open("websites.txt", "r")
for website in websites:
    webbrowser.open(website)
