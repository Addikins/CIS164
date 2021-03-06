import datetime

# According to python 3.8 documentation datetime.datetime.weekday returns an integer from 0-6 starting on Monday
days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def user_greeting(username, date):
    # Return greeting as string and access the specified index of the days_of_the_week array
    return "Hello " + username + " I hope you are having a great " + days_of_the_week[date.weekday()]


# Use case example


print(user_greeting("Adhem", datetime.datetime.today()))
