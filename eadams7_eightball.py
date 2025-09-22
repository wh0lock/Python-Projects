# Emily Adams
# Magic Eight Ball
# Started September 1, 2025, due September 5, 2025
# This project is an interactive fortune teller, based on the "Magic Eight Ball" toy.

import random
fortunes = ["Yes.", "No.", "Never in a million years.", "It could happen.", "Highly doubtful.", "Very possible.", "Likely.", "Unlikely."]
print(f"What will you do?\n 1: print all the fortunes\n 2: print a specific fortune\n 3: get a random fortune")
choice = input("Please choose 1, 2, or 3: ")
if choice == "1":
    print("YOUR FORTUNES")
    for index, fortune in enumerate(fortunes):
        print(f"{index}) {fortune}")
elif choice == "2":
    which = input("What number do you want? (0-7): ")
    intWhich = int(which)
    if intWhich > 7:
        print("That's too high of a number.")
    else:
        print(fortunes[intWhich])
elif choice == "3":
    input("Your question: ")
    randomNumber = random.randrange(8)
    print(fortunes[randomNumber])
else:
    print("I don't know what you want from me.")
    
