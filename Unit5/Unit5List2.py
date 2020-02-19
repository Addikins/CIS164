sales = []
value = int

print("Please enter your sales one at a time.\nWhen you are finished enter '0'")
while value != 0:
    value = int(input("Enter your sale amount: "))

    if value == 0:
        break
    sales.append(value)

total = sum(sales)
print("Your total sales: ", total)

sales.sort()
print("Individual sales: ", sales)

sales.sort(reverse=True)
print("Same sales, backwards: ", sales)


def check_for_100():
    if 100 in sales:
        return "Yes, 100 is in the list"
    else:
        return "No, 100 is not in the list"


print(check_for_100())
