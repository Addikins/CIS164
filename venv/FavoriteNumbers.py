print("Hello!\nThis program takes in two of your favorite numbers, adds them together, and then returns their sum."
      "\nTo begin, please enter one of your favorite numbers:")
favNum1: int = int(input())
print("Great, looks like you gave me", favNum1, "!\nNow, please give me another number you love:")
favNum2: int = int(input())
print("Perfect!\nNow let's take", favNum1, "and add it to", favNum2, ".")
print(favNum1, "+", favNum2, "=", favNum1 + favNum2, "!")
