# Blackjack Game
This is a simple Blackjack game developed in Python. <br />
This game simulates the popular casino card game, in which the objective is to get a hand value of 21 or as close to 21 as possible without exceeding it.<br />

## Requirements
This game requires Python 3.x to be installed in your computer. It uses the following modules:

classes.deck<br />
classes.player<br />
<br />
## How to Run
To run the game, simply execute the blackjack.py file in the terminal or command prompt. <br />
The game will start and you will be prompted to enter the player name.

python blackjack.py <br />
<br />
## How to Play
The game will start by shuffling the deck and dealing two cards to both the player and the dealer. <br />
The player's cards will be visible, but only one of the dealer's cards will be visible to the player.<br />

The player will then have the option to hit (receive another card) or stand (keep the current hand value).<br />
If the player hits and exceeds a hand value of 21, the game is over and the dealer wins.<br />

After the player's turn, the dealer will reveal their hidden card and continue to draw until their hand value is 17 or higher. If the dealer exceeds a hand value of 21, the player wins.

The player wins if they have a hand value higher than the dealer's, but not exceeding 21. <br />
If the player's hand value equals 21 (blackjack), the player automatically wins.<br />
After each game, the player will be prompted to continue playing or quit.<br />

## Classes
This program uses the following classes:

### Deck
This class represents a deck of 52 cards. It has the following attributes:

cards: a list of tuples representing each card in the deck<br />
cardsType: a list of strings representing the card types (e.g. "Hearts", "Spades", "Diamonds", "Clubs")<br />
cardsValue: a dictionary mapping each card to its numeric value<br />
And the following methods:<br />

shuffleCards: shuffles the deck<br />
extracingCard: extracts a card from the deck and removes it from the cards list<br />
resetCards: resets the deck to its original state<br />
<br />
### Player
This class represents a player. <br />
It has the following attributes:

name: a string representing the player's name<br />
hand: a list of tuples representing the player's hand<br />
sumOfCards: an integer representing the sum of the player's hand<br />
score: an integer representing the player's score<br />
And the following methods:<br />

player_got_ace: handles the case where the player is dealt an ace<br />
hit: adds a card to the player's hand and updates the sum of the hand values<br />
player_move: handles the player's move (hit or stand)<br />
players_sum_of_cards: prints the sum of the player's hand values<br />
player_lost: prints a message indicating the player has lost<br />
add_score: increments the player's score by 1<br />
### Acknowledgements
This game was developed with the help of the following resources:<br />

Python Classes - w3schools<br />
Blackjack rules - Bicycle Cards.<br />
