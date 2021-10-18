#card shuffler and dealer

#tests:
    #test1 - shuffles a pack of cards
    #test2 - deals a card and once dealt removes from the pack
    #test3 - deals a hand of cards equal to parameters set

import random

StandardPack = [
    "A-H", "K-H", "Q-H", "J-H", "10-H", "9-H", "8-H", "7-H", "6-H", "5-H", "4-H", "3-H", "2-H",
    "A-S", "K-S", "Q-S", "J-S", "10-S", "9-S", "8-S", "7-S", "6-S", "5-S", "4-S", "3-S", "2-S",
    "A-C", "K-C", "Q-C", "J-C", "10-C", "9-C", "8-C", "7-C", "6-C", "5-C", "4-C", "3-C", "2-C",
    "A-D", "K-D", "Q-D", "J-D", "10-D", "9-D", "8-D", "7-D", "6-D", "5-D", "4-D", "3-D", "2-D"
    ]

startPackNotShuffled = [
    "A-H", "K-H", "Q-H", "J-H", "10-H", "9-H", "8-H", "7-H", "6-H", "5-H", "4-H", "3-H", "2-H",
    "A-S", "K-S", "Q-S", "J-S", "10-S", "9-S", "8-S", "7-S", "6-S", "5-S", "4-S", "3-S", "2-S",
    "A-C", "K-C", "Q-C", "J-C", "10-C", "9-C", "8-C", "7-C", "6-C", "5-C", "4-C", "3-C", "2-C",
    "A-D", "K-D", "Q-D", "J-D", "10-D", "9-D", "8-D", "7-D", "6-D", "5-D", "4-D", "3-D", "2-D"
    ]


        
def DealACard(packToDealFrom):

    cardToDealIndex = random.randint(0,len(packToDealFrom))
    cardToDeal = packToDealFrom[cardToDealIndex]
    packToDealFrom.remove(cardToDeal)
    return cardToDeal, packToDealFrom

def shuffleCardPack(packList):
    
    shuffledPack = random.sample(packList, len(packList))
    print("pack shuffled complete")
    return shuffledPack

def dealAHand(packToDealFrom, numberOfCards):
    
    hand = []
    
    for card in range(0, numberOfCards):
        nextCard = DealACard(packToDealFrom)
        hand.append(nextCard[0])
        
    return hand

def test1ShufflePack(startingPack, endingPack):
        
    correspondingItems = 0
    nonCorrespondingItems = 0

    counter = 0
    for card in startingPack:

        if card == endingPack[counter]:
            correspondingItems = correspondingItems + 1
            counter = counter + 1
        else:
            nonCorrespondingItems = nonCorrespondingItems  + 1
            counter = counter + 1
    
    if nonCorrespondingItems >= 1:
        mathOrderCheck = "NotMatching"
    else:
        mathOrderCheck = "Matching"
    
    if len(startingPack) == len(endingPack) and mathOrderCheck == "NotMatching":
        print("Test 1 passed")
    else:
        print("Test 1 failed")

def test2DealACard(packToDealFrom):
    
    startingNumber = len(packToDealFrom)
    cardAndRevisedPack = DealACard(packToDealFrom)
    endingNumber = len(packToDealFrom)
    
    if startingNumber - endingNumber == 1:
        print("Test 2 passed")
    else:
        print("Test 2 failed")
        
def test3DealAHand(packToDealFrom, numberOfCards):
    
    cardHand = dealAHand(packToDealFrom, numberOfCards)
    
    cardChecker = 0
    for card in cardHand:
        if card in StandardPack:
            cardChecker = cardChecker +1
        else:
            null
    
    if len(cardHand) == numberOfCards and cardChecker == numberOfCards:
        print("Test 3 passed")
    else:
        print("Test 3 failed")

def main():
    
    #shuffledPack = shuffleCardPack(startPackNotShuffled)
    #cardDeal = DealACard(shuffledPack)
    #cardHand = dealAHand(startPackNotShuffled, 10)
    
    #test1ShufflePack(startPackNotShuffled, shuffledPack)
    #test2DealACard(startPackNotShuffled)
    #test3DealAHand(startPackNotShuffled, 10)
    
main()