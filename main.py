# use classes to define the player and the deck
from classes.deck import Deck
from classes.player import Player
# from classes.logic import Logic

import time


def timeOut(sec):
    time.sleep(sec)


def welcome_message():
    print('---------------------------------------')
    print('Welcome to my Blackjack game, Good luck!')
    print('---------------------------------------')


def start_game():
    return int(input(('To start game, press:1  ')))


###### creating objects of users and deck #################
def creating_player(name):
    if name == 'Dealer':
        return Player(name)
    return Player(input('Player name: '))


def reset_deck():
    return Deck


def whosTurn(player):
    print(f'{player.name} turn')


def hit(our_deck):
    my_card = our_deck.extracingCard(our_deck.cards, our_deck.extractedCards, our_deck.cardsType, our_deck.cardsValue)
    return my_card


def player_move(player, current_card):
    player.hand.append(current_card)
    current_card_value = current_card[0]
    if current_card_value == 'Ace':
        current_card_value = player_got_ace(player)
    else:
        if len(current_card_value) > 1:
            current_card_value = 10
        else:
            current_card_value = int(current_card_value)

    player.sumOfCards += current_card_value
    # number = player.hand.get
    # type = player.hand[len(player.hand)][1]
    print(f'{player.name} hand is: {player.hand}')
    timeOut(0.5)


def player_got_ace(player):
    if (player.name == 'Dealer'):
        if player.sumOfCards <= 10:
            return 11
        else:
            return 1
    else:
        return int(input('You got Ace! use as 11 or 1? '))


def players_sum_of_cards(player):
    print(f'{player.name} sum of cards is: {player.sumOfCards}\n')


def player_lost(player):
    print(f'{player.name} has lost with total card of: {player.sumOfCards}\n')


def add_score(player):
    player.score += 1


def hitOrPass():
    return int(input('Enter 1 - Hit me | Enter 0 - Pass:  '))


def reset_game(player, dealer, deck):
    player.sumOfCards = 0
    player.hand.clear()
    dealer.sumOfCards = 0
    dealer.hand.clear()
    deck = Deck


def current_score(player, dealer):
    player_score = player.score
    dealer_score = dealer.score
    if player_score > dealer_score:
        # print(f'{dealer_score}:{player_score}  {player.name} is leading with the score of {player_score}')
        print(f'{dealer_score}:{player_score}  {player.name} is leading with the score of {player_score}')
    else:
        print(f'{dealer_score}:{player_score}  {dealer.name} is leading with the score of {dealer_score}')
    if player_score == dealer_score:
        print(f'{dealer_score}:{player_score}  Its a draw between {dealer.name} and {player.name}')


def check_score_higher_than_21(player):
    timeOut(1)
    if player.sumOfCards > 21:
        return 1
    if player.sumOfCards == 21:
        return 2
    return False


def continue_playing():
    return int(input('Continue - 1 | Quit game - 0 : '))


def stop_game(play):
    print('Thank you for playing, see you next time.')
    return 0


def take_turn(player):
    whosTurn(player)
    if player.name == 'Dealer':
        player_move(player, hit(our_deck))
    else:
        pass
    players_sum_of_cards(player)


def take_hit(player, deck):
    player_move(player, hit(deck))


def blackjack(player):
    print(f'{player.name} got blackjack!')


def play_game(play):
    while play:
        take_turn(dealer)
        if check_score_higher_than_21(dealer) == 1:
            player_lost(dealer)
            add_score(player1)
            if not continue_playing():
                play = stop_game(play)
            if play:
                reset_game(player1, dealer, our_deck)
                current_score(player1, dealer)
            elif check_score_higher_than_21(dealer) == 2:
                blackjack(dealer)
                player_lost(player1)
                add_score(dealer)
        else:
            take_turn(player1)
            action = hitOrPass()
            if action:
                take_hit(player1, our_deck)
                if check_score_higher_than_21(player1) == 1:
                    player_lost(player1)
                    add_score(dealer)
                    if not continue_playing():
                        play = stop_game(play)
                    if play:
                        reset_game(player1, dealer, our_deck)
                        current_score(player1, dealer)
                elif check_score_higher_than_21(player1) == 2:
                    blackjack(player1)
                    player_lost(dealer)
                    add_score(player1)



################################## Welcome message and setting variables###############################################################
welcome_message()
play = start_game()
player1 = creating_player('')
dealer = creating_player('Dealer')
our_deck = reset_deck()

print('Shuffling  deck . . .\n')
timeOut(1.5)
play_game(play)

################################## Game started #####################################################################################


# while play:
#     whosTurn(dealer)
#     player_move(dealer, hit(our_deck))
#     players_sum_of_cards(dealer)
#     if check_score_higher_than_21(dealer):
#         player_lost(dealer)
#         add_score(player1)
#         if not continue_playing():
#             play = stop_game(play)
#         if play:
#             reset_game(player1, dealer, our_deck)
#             current_score(player1, dealer)
#     # continue playing next turn
#     else:
#         whosTurn(player1)
#         players_sum_of_cards(player1)
#         action = hitOrPass()
#         # if user decide to Hit me
#         if action:
#             player_move(player1, hit(our_deck))
#             if check_score_higher_than_21(player1):
#                 player_lost(player1)
#                 add_score(dealer)
#                 # if user decide to keep on playing
#                 if not continue_playing():
#                     play = stop_game(play)
#                 if play:
#                     reset_game(player1, dealer, our_deck)
#                     current_score(player1, dealer)
#         # user pass card
#         elif not action:
#             pass
