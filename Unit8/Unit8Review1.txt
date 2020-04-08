def dividing(denominator):
    try:
        return 100 / denominator
    except ZeroDivisionError:
        print("You tried to divide by zero!")
