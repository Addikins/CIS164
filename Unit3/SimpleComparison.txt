import random


def check_if_number():
    while True:
        try:
            x = int(input())
            return x
        except:
            print("That's not a number!")


lineSpacing = "\n" * 10

print("Let's play a little game.\nGive me a number to get started:")
inputNum1 = check_if_number()

print("\nGreat!\nNow give me another:")
inputNum2 = check_if_number()

while inputNum2 <= inputNum1:
    print("I'm sorry, I need a higher number:")
    inputNum2 = check_if_number()

print(lineSpacing, "Perfect!", lineSpacing)

randomNumber = random.randint(inputNum1, inputNum2)

print("I'm thinking of a number between ", inputNum1, " and ", inputNum2,
      "\nWhat do you think it is? Take your best guess!")
guess = check_if_number()

while guess != randomNumber:
    if guess < randomNumber:
        print("Your guess is a little low.")
        guess = check_if_number()

    if guess > randomNumber:
        print("Your guess is a too high.")
        guess = check_if_number()

print(lineSpacing, "Congratulations! Your guess '", guess, "' is correct!", lineSpacing, "Thanks for playing!")
