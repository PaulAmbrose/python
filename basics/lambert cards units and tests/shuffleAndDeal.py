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

endPackShuffled = []

def test1ShufflePack():
    print("Start of test: the pack is " + str(startPackNotShuffled))
    print("Number of cards is " + str(len(startPackNotShuffled)))
        
        shuffleCardPack()
    
    print("End of test: the pack is " + str(len(endPackShuffled)))
    print("Number of cards is " + str(len(endPackShuffled)))
    
    correspondingItems = 0
    nonCorrespondingItems = 0
    
    for card in startPackNotShuffled:
        if startPackNotShuffled != endPackShuffled:
            correspondingItems = correspondingItems + 1
        else:
            nonCorrespondingItems = nonCorrespondingItems  + 1
    
    if nonCorrespondingItems > 1:
        mathOrderCheck = "NotMatching"
    else:
        mathOrderCheck = "Matching"
    
    if len(startPackNotShuffled) == len(endPackShuffled) and mathOrderCheck == "NotMatching":
        print("Test passed")
    else:
        print("Test failed")

def shuffleCardPack():
    

    
def main():
    
    test1ShufflePack()
    
main()