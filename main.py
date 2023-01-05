# use classes to define the player and the deck
from classes.deck import Deck
from classes.player import Player
# from classes.logic import Logic

import time


def timeOut(sec):
    time.sleep(sec)


ourDeck = Deck
player1 = Player('Ron')
dealer = Player('Dealer')


def hit(ourDeck):
    my_card = ourDeck.extracingCard(ourDeck.cards, ourDeck.extractedCards, ourDeck.cardsType, ourDeck.cardsValue)
    return my_card


def store_data(player, currentCard):
    player.hand.append(currentCard)
    # currentCardValue = currentCard[0]
    if currentCard[0] == 'Ace':
        currentCardValue = int(input('You got Ace! use as 10 or 1? '))
    else:
        if len(currentCard[0]) > 2:
            currentCardValue = 10
        else:
            currentCardValue = int(currentCard[0])
    player.sumOfCards += currentCardValue
    print(f'{player.name}s hand is: {player.hand} Total sum: {player.sumOfCards}')
    timeOut(0.5)


def checkScoreHigherThan21(player):
    timeOut(1)
    if player.sumOfCards > 21:
        return True
    return False


# player move
play = True
print('---------------------------------------')
print('Welcom to my Blackjack game, Good luck!')
print('---------------------------------------\n')
timeOut(2)
while play:
    store_data(dealer, hit(ourDeck))
    print(f'Dealers sum of card is: {dealer.sumOfCards}')
    if not checkScoreHigherThan21(dealer):
        pass
    else:
        print(f'{dealer.name} has lost with total card of: {dealer.sumOfCards}')
        play = False
    if play:
        print(f'\nPlayer sum of cards is:  {player1.sumOfCards} ')
        action = input('Enter 1 - Hit me | Enter 2 - Pass:  ')
        if int(action) == 1:
            store_data(player1, hit(ourDeck))
            print('\n')
            if checkScoreHigherThan21(player1):
                print(f'{player1.name} has lost with total card of: {player1.sumOfCards}')
                player1.score += 1
                input('Quit game - 0 | Continue - 1')
                play = False
        elif int(action) == 2:
            pass
