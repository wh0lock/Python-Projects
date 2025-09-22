# Emily Adams
# Number Guesser 
# Started September 9, 2025, Due September 12, 2025
# This project generates a random number for the user to guess.

import random
secret = random.randint(1,100)
tries = 0
keepGoing = True
while keepGoing:
    tries += 1
    userGuess = input("What is your guess? ")
    correct = userGuess.isnumeric()
    if correct:
        userGuessInt = int(userGuess)
        if userGuessInt > secret:
            print("Too high")
        elif userGuessInt < secret:
            print("Too low")
        else:
            print(f"You got it in {tries} turns!")
            print("You win!")
            keepGoing = False
    else:
        if tries >= 7:
            print("You should be able to solve this in 7 tries or less.")
            print(f"You lose! The number was {secret}.")
            keepGoing = False
    if correct == False:
        print("That's not a number...")
    
        
