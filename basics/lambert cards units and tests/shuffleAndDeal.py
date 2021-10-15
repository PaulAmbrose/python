#card shuffler and dealer

#tests:
    #test1 - shuffles a pack of cards
    #test2 - deals a card and once dealt removes from the pack
    #test3 - deals another card from cards remaining

import random

startPackNotShuffled = [
    "A-H", "K-H", "Q-H", "J-H", "10-H", "9-H", "8-H", "7-H", "6-H", "5-H", "4-H", "3-H", "2-H",
    "A-S", "K-S", "Q-S", "J-S", "10-S", "9-S", "8-S", "7-S", "6-S", "5-S", "4-S", "3-S", "2-S",
    "A-C", "K-C", "Q-C", "J-C", "10-C", "9-C", "8-C", "7-C", "6-C", "5-C", "4-C", "3-C", "2-C",
    "A-D", "K-D", "Q-D", "J-D", "10-D", "9-D", "8-D", "7-D", "6-D", "5-D", "4-D", "3-D", "2-D"
    ]

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
        print("Test passed")
    else:
        print("Test failed")

def DealACard(packToDealFrom):

    cardToDealIndex = random.randint(0,len(packToDealFrom))
    cardToDeal = packToDealFrom[cardToDealIndex]
    packToDealFrom.remove(cardToDeal)
    return cardToDeal, packToDealFrom

def shuffleCardPack(packList):
    
    shuffledPack = random.sample(packList, len(packList))
    print("pack shuffled complete")
    return shuffledPack

def main():
    
    shuffledPack = shuffleCardPack(startPackNotShuffled)
    cardDeal = DealACard(shuffledPack)
    print("Card Dealt " + cardDeal[0])
    print("new Pack " + str(cardDeal[1]))
    #test1ShufflePack(startPackNotShuffled, shuffledPack)
    
main()