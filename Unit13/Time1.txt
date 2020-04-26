import time
import datetime


def timeReporting(sleep_time):
    current = time.localtime()
    print("The Current Date is: ", current.tm_mon, "/", current.tm_mday, "/", current.tm_year,
          "\nAlternatively, using the DateTime module, the Current Date is: ", today.month, "/", today.day, "/", today.year,
          "\nThe Current Time is: ", current.tm_hour, ":", current.tm_min, ":", current.tm_sec)

    while sleep_time > 0:
        print(sleep_time, "...")
        sleep_time -= 1
        time.sleep(1)

    current = time.localtime()
    print("The Current Date is: ", current.tm_mon, "/", current.tm_mday, "/", current.tm_year,
          "\nThe Current Time is: ", current.tm_hour, ":", current.tm_min, ":", current.tm_sec)


today = datetime.date.today()

timeReporting(5)
