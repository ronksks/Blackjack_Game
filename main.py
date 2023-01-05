# use classes to define the player and the deck
from classes.deck import Deck
from classes.player import Player
# from classes.logic import Logic

import time


def timeOut(sec):
    time.sleep(sec)


def startGame():
    return int(input(('To start game, press:1  ')))


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


def continuePlaying():
    return bool(input('Quit game - 0 | Continue - 1 : '))


def setUpGame():
    pass


def welcomeMessage():
    print('---------------------------------------')
    print('Welcome to my Blackjack game, Good luck!')
    print('---------------------------------------')

###### creating objects of users and deck #################
def creatingPlayer(name):
    if name == 'Dealer':
        return Player(name)
    return Player(input('Player name: '))
def creatingDeck():
    return Deck


game = setUpGame()
print(game)


################################## Welcom message #####################################################################################
welcomeMessage()
play = startGame()
player1 = creatingPlayer('')
dealer = creatingPlayer('Dealer')
ourDeck = creatingDeck()

def playersSumOfCards(player):
    print(f'{player.name} sum of card is: {player.sumOfCards}\n')

def playerLost(player):
    print(f'{player.name} has lost with total card of: {player.sumOfCards}\n')


print('Shuffling  deck . . .\n')
timeOut(2)
################################## Game started #####################################################################################
while play:
    store_data(dealer, hit(ourDeck))
    playersSumOfCards(dealer)
    # print(f'Dealers sum of card is: {dealer.sumOfCards}')
    if not checkScoreHigherThan21(dealer):
        pass
    else:
        playerLost(dealer)
        if not continuePlaying():
            play = False
    if play:
        playersSumOfCards(player1)
        action = input('Enter 1 - Hit me | Enter 2 - Pass:  ')
        if int(action) == 1:
            store_data(player1, hit(ourDeck))
            print('\n')
            if checkScoreHigherThan21(player1):
                playerLost(player1)
                player1.score += 1
                if not continuePlaying():
                    play = False
        elif int(action) == 2:
            pass
