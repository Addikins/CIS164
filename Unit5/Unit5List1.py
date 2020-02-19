days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
selection = int

for day in days:
    print(day)

print("\nPlease choose a day of the week.\nFor example, for Sunday enter 1, for Saturday enter 7")

while selection not in range(1, 7):
    selection = int(input("Enter your selection: "))

print("\nYou chose ", days[selection - 1])
