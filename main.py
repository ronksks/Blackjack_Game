# use classes to define the player and the deck
from classes.deck import Deck
from classes.player import Player
# from classes.logic import Logic

import time


def timeOut(sec):
    time.sleep(sec)


def welcomeMessage():
    print('---------------------------------------')
    print('Welcome to my Blackjack game, Good luck!')
    print('---------------------------------------')


def startGame():
    return int(input(('To start game, press:1  ')))


###### creating objects of users and deck #################
def creatingPlayer(name):
    if name == 'Dealer':
        return Player(name)
    return Player(input('Player name: '))


def resetDeck():
    return Deck


def whosTurn(player):
    print(f'{player.name} turn')


def hit(ourDeck):
    my_card = ourDeck.extracingCard(ourDeck.cards, ourDeck.extractedCards, ourDeck.cardsType, ourDeck.cardsValue)
    return my_card


def playerMove(player, currentCard):
    player.hand.append(currentCard)
    currentCardValue = currentCard[0]
    if currentCardValue == 'Ace':
        currentCardValue = int(input('You got Ace! use as 11 or 1? '))
    else:
        if len(currentCardValue) > 1:
            currentCardValue = 10
        else:
            currentCardValue = int(currentCardValue)

    player.sumOfCards += currentCardValue
    print(f'{player.name}s hand is: {player.hand}')
    timeOut(0.5)


def playersSumOfCards(player):
    print(f'{player.name} sum of cards is: {player.sumOfCards}\n')


def playerLost(player):
    print(f'{player.name} has lost with total card of: {player.sumOfCards}\n')


def addScore(player):
    player.score += 1


def hitOrPass():
    return int(input('Enter 1 - Hit me | Enter 0 - Pass:  '))


def resetGame(player, dealer, deck):
    player.sumOfCards = 0
    player.hand.clear()
    dealer.sumOfCards = 0
    dealer.hand.clear()
    deck = Deck


def currentScore(player, dealer):
    playerScore = player.score
    dealerScore = dealer.score
    if playerScore > dealerScore:
        print(f'{dealerScore}:{playerScore}  {player.name} is leading with the score of {playerScore}')
    else:
        print(f'{dealerScore}:{playerScore}  {dealer.name} is leading with the score of {dealerScore}')
    if playerScore == dealerScore:
        print(f'{dealerScore}:{playerScore}  Its a draw between {dealer.name} and {player.name}')


def checkScoreHigherThan21(player):
    timeOut(1)
    if player.sumOfCards > 21:
        return True
    return False


def continuePlaying():
    return int(input('Continue - 1 | Quit game - 0 : '))


def stopGame(play):
    print('Thank you for playing, see you next time.')
    return 0


################################## Welcom message and setting variables###############################################################
welcomeMessage()
play = startGame()
player1 = creatingPlayer('')
dealer = creatingPlayer('Dealer')
ourDeck = resetDeck()

print('Shuffling  deck . . .\n')
timeOut(1.5)
################################## Game started #####################################################################################

while play:
    whosTurn(dealer)
    playerMove(dealer, hit(ourDeck))
    # timeOut(0.1)
    playersSumOfCards(dealer)
    if checkScoreHigherThan21(dealer):
        playerLost(dealer)
        addScore(player1)
        if not continuePlaying():
            play = stopGame(play)
        if play:
            resetGame(player1, dealer, ourDeck)
            currentScore(player1, dealer)
    # continue playing next turn
    else:
        whosTurn(player1)
        playersSumOfCards(player1)
        action = hitOrPass()
        # if user decide to Hit me
        if action:
            playerMove(player1, hit(ourDeck))
            if checkScoreHigherThan21(player1):
                playerLost(player1)
                addScore(dealer)
                # if user decide to keep on playing
                if not continuePlaying():
                    play = stopGame(play)
                if play:
                    resetGame(player1, dealer, ourDeck)
                    currentScore(player1, dealer)
        # user pass card
        elif not action:
            pass
