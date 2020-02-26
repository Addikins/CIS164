months = {"January": "Jane", "February": "Fred", "March": "Maria", "April": "Anne", "May": "Mary", "June": "Juniper",
          "July": "Julia", "August": "Autumn", "September": "Steven", "October": "Octavio", "November": "Nancy",
          "December": "Devin"}

print("Each month has a secret name. Choose a month to find it out!")

selection = input("Please enter a month: ").capitalize()

print(selection + "'s secret name is " + months[selection] + "!")
