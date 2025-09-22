""" cards.py
    demonstrates functions
    manage a deck of cards db

"""
import random

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def main():
    cardDB = initCards()

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB)

    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)
    
def initCards():
    cardDB = []
    for i in range(NUMCARDS):
        cardDB.append(0)
    return cardDB

def showDB(cardDB):
    for cardNum, location in enumerate(cardDB):
        print(f"{cardNum:4}: {getCardName(cardNum):20} {HANDS[location]}")
    print()
    
def getCardName(cardNum):
    suit = cardNum // 13
    rank = cardNum % 13
    cardName = f"{RANKNAME[rank]} of {SUITNAME[suit]}"
    return cardName
    
def assignCard(cardDB, hand):
    cardNum = random.randrange(NUMCARDS)
    keepGoing = True
    while keepGoing:
        if cardDB[cardNum] == 0:
            cardDB[cardNum] = hand
            keepGoing = False
    
def showHand(cardDB, hand):
    print(f"Cards in {HANDS[hand]} hand: ")
    for cardNum, location in enumerate(cardDB):
        if location == hand:
            print(f"	{getCardName(cardNum)}")         
    print()
 
main()