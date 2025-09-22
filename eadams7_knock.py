# Emily Adams
# Knock-Knock Joke
# Started August 28, 2025, due August 29, 2025
# This project is an interactive knock-knock joke.

name = input("What is your name? ")
answer = input(f"Hey, {name}, do you want to hear a joke? (Y/N) ").upper()
if answer == "Y":
    print("Knock knock.")
    who = input().upper()
    if who == "WHO'S THERE?":
        print("Iran.")
        answer2 = input().upper()
        if answer2 == "IRAN WHO?":
            print("Iran here. I'm tired!")
        else:
            print("You were supposed to say 'Iran who?'")
    else:
        print("You were supposed to say 'Who's there?'")
else:
    print("It was going to be really funny.")
