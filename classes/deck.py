import random
import math



# Deck is set like this:
# [A,A,A,A,2,2,2,2,3,3,3,3,....,14,14,14,14]

class Deck:
    cards = [1] * 52
    extractedCards = []
    cardsType = {
        0: 'Heart ♥',
        1: 'Dimond ♦',
        2: 'Spades ♠',
        3: 'Clubs ♣'
    }
    cardsValue = {
        0: 'Ace',
        1: '2',
        2: '3',
        3: '4',
        4: '5',
        5: '6',
        6: '7',
        7: '8',
        8: '9',
        9: '10',
        10: 'Jack',
        11: 'Queen',
        12: 'King',
    }

    def __init__(self, numOfCards=52):
        self.numOfCards = numOfCards

    def shuffel_deck(self):
        pass

    # reseting deck
    # for i in range(0, 52):
    #     cards[i] = 1

    def extracingCard(cards, extractedCards, cardsType, cardsValue):
        validCardExtraction = True
        itterations = 0
        while (validCardExtraction):
            cardtoExtract = random.randint(0, 51)
            if cardtoExtract not in extractedCards:
                extractedCards.append(cardtoExtract)
                cards[cardtoExtract] = 0
                validCardExtraction = False
                cardValue = cardsValue.get(math.floor(cardtoExtract / 4))
                cardType = cardsType.get(cardtoExtract % 4)
                # returns a tupel
                # returns a tupel

        return (cardValue, cardType)

    # def hit_card():
    #     my_card = extracingCard(extractedCards, cards, cardsType)
    #     return my_card
